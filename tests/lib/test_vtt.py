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


def test_join_multilines():
    with open("tests/sample/join_multilines.vtt", "r") as f:
        text = f.read()
        payload = vtt.extract_payload(text)
        joined_data = vtt.join_multilines(payload)
        expected_value = [
            {
                "start": "00:02:12.750",
                "end": "00:02:15.291",
                "text": " My name is Walter Hartwell White.",
            },
            {"start": "00:10:40.750", "end": "00:10:43.208", "text": " ALL: Surprise!"},
            {
                "start": "00:10:59.291",
                "end": "00:11:01.500",
                "text": " She's not showing at all, is she?",
            },
            {
                "start": "00:11:13.667",
                "end": "00:11:18.500",
                "text": " I mean, unless you're talking, what, Plus P Plus loads, you can forget the 9 mil, all right?",
            },
        ]
        assert joined_data == expected_value
