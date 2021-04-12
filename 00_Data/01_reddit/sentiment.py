from transformers import BertForSequenceClassification, BertTokenizer
import torch
'''
Sources:
https://towardsdatascience.com/how-to-apply-transformers-to-any-length-of-text-a5601410af7f
https://www.youtube.com/watch?v=yDGo9z_RlnE
'''
tokenizer = BertTokenizer.from_pretrained('ProsusAI/finbert')
model = BertForSequenceClassification.from_pretrained('ProsusAI/finbert')


def get_sentiment(txt):
    if type(txt) is not str:
        raise ValueError('txt')

    tokens = tokenizer.encode_plus(txt, add_special_tokens=False, return_tensors='pt')

    input_id_chunks = tokens['input_ids'][0].split(510)
    mask_chunks = tokens['attention_mask'][0].split(510)

    input_id_chunks = list(input_id_chunks)
    mask_chunks = list(mask_chunks)

    for i in range(len(input_id_chunks)):
        input_id_chunks[i] = torch.cat([
            torch.Tensor([101]), input_id_chunks[i], torch.Tensor([102])
        ])
        mask_chunks[i] = torch.cat([
            torch.Tensor([1]), mask_chunks[i], torch.Tensor([1])
        ])
        # get required padding length
        pad_len = 512 - input_id_chunks[i].shape[0]
        # check if tensor length satisfies required chunk size
        if pad_len > 0:
            # if padding length is more than 0, we must add padding
            input_id_chunks[i] = torch.cat([
                input_id_chunks[i], torch.Tensor([0] * pad_len)
            ])
            mask_chunks[i] = torch.cat([
                mask_chunks[i], torch.Tensor([0] * pad_len)
            ])

    input_ids = torch.stack(input_id_chunks)
    attention_mask = torch.stack(mask_chunks)

    input_dict = {
        'input_ids': input_ids.long(),
        'attention_mask': attention_mask.int()
    }

    outputs = model(**input_dict)

    probs = torch.nn.functional.softmax(outputs[0], dim=-1)

    mean = probs.mean(dim=0)

    label = ['pos', 'neg', 'neut'][torch.argmax(mean).item()]

    return [label, round(mean[0].item(), 2), round(mean[1].item(), 2), round(mean[2].item(), 2)]


if __name__ == '__main__':
    get_sentiment(txt=None)
