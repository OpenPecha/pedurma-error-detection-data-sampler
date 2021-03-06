from pathlib import Path

from pedurma.preview import get_reconstructed_text


def get_collated_text(text_id):
    # try:
    collated_text, _ = get_reconstructed_text(text_id, bdrc_img=False)
    # except:
    #     collated_text = {}
    return collated_text
    

if __name__ == "__main__":
    collated_text = Path('./ludup_text.txt').read_text(encoding='utf-8')
    collated_text_list = list(Path('./collated_text').iterdir())
    collated_text_list.sort()
    collated_text_list = [text_id.stem[:-5] for text_id in collated_text_list]
    collated_text_ids = collated_text.splitlines()
    # collated_text_ids = ["Q5811",]
    for collated_text_id in collated_text_ids[72:]:
        # if collated_text_id in collated_text_list:
        #     continue
        collated_text = get_collated_text(collated_text_id)
        while not collated_text:
            collated_text = get_collated_text(collated_text_id)
        for vol_id, text in collated_text.items():
            Path(f'./ludup_text/{collated_text_id}_{vol_id}.txt').write_text(text, encoding='utf-8')
        print(f'{collated_text_id} completed..')
