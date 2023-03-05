from lines.lib import vtt

# Breaking Bad s1 e1 on Netflix
url = "https://ipv4-c003-itm001-k-opticom-isp.1.oca.nflxvideo.net/?o=1&v=121&e=1675609223&t=fr-uZkiRvIUukvSmUZ7cohOOE154ZzZvoglYsKlh5bcx5GNRrPRLiK2KVGPEaZR7Zo_VGlh--TxZ9x_AgHTwTTfuXo7rt5_zc8Ju84QrJdbfAmUDADtMA4l46jBcwWltfIrgF7Mhj_d4E0XerDCfXeDK-LDuQaAsRJSOEKtHhdejm9GICuzDBwy2m2F2qJDvKFkGbGDxG5ddZydAEeBUuIGwk4Y47pYeA-hRkfZZ-zFnHw"


def test_fetch():
    path = "tests/sample/fetch.vtt"
    assert type(vtt.fetch(path)) == str


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
            {"start": "00:00:13.333", "end": "00:00:16.542", "text": "[♪♪♪]"},
            {
                "start": "00:25:52.125",
                "end": "00:25:56.041",
                "text": "No, I'm not. I'm made",
            },
            {
                "start": "00:25:52.125",
                "end": "00:25:56.041",
                "text": "of flesh and bone and meaty bits!",
            },
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
            {"start": "00:21:27.709", "end": "00:21:29.917", "text": " [♪♪♪]"},
            {
                "start": "00:22:13.291",
                "end": "00:22:16.125",
                "text": " [BUTTONS BEEPING]",
            },
            {
                "start": "00:22:16.125",
                "end": "00:22:17.917",
                "text": " [PHONE RINGING]",
            },
            {
                "start": "00:55:12.166",
                "end": "00:55:15.875",
                "text": " ♪ I'm walking out for love ♪",
            },
            {
                "start": "00:55:15.875",
                "end": "00:55:19.333",
                "text": " ♪ I'm walking out really down In a cool breeze ♪",
            },
        ]
        assert joined_data == expected_value
