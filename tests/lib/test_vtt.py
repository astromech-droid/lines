from lines.lib import vtt

# Breaking Bad s1 e1 on Netflix
url = "https://ipv4-c003-itm001-k-opticom-isp.1.oca.nflxvideo.net/?o=1&v=121&e=1675609223&t=fr-uZkiRvIUukvSmUZ7cohOOE154ZzZvoglYsKlh5bcx5GNRrPRLiK2KVGPEaZR7Zo_VGlh--TxZ9x_AgHTwTTfuXo7rt5_zc8Ju84QrJdbfAmUDADtMA4l46jBcwWltfIrgF7Mhj_d4E0XerDCfXeDK-LDuQaAsRJSOEKtHhdejm9GICuzDBwy2m2F2qJDvKFkGbGDxG5ddZydAEeBUuIGwk4Y47pYeA-hRkfZZ-zFnHw"


def test_fetch():
    assert type(vtt.fetch(url)) == str
    assert vtt.fetch("https://google.com") is None


def test_save(tmp_path):
    text = "test_save"
    path = tmp_path / "test_save.txt"

    assert vtt.save(text, path) is True


def test_download(tmp_path):
    path = tmp_path / "test_download.txt"
    assert vtt.download(url, path) is True


def test_extract_payload():
    with open("tests/sample/extract_payload.vtt", "r") as f:
        text = f.read()
        payload = vtt.extract_payload(text)
        excepted_value = [
            {"start": "00:00:13.333", "end": "00:00:16.542", "text": "[♪♪♪]"}
        ]
        assert payload == excepted_value
