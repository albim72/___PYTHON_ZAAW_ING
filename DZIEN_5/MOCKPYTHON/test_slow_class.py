from main import slow_dataset

def test_mocking_class(mocker):
    expected = "xyz"
    def mock_load(self):
        return "xyz"
    mocker.patch(
        'main.Dataset.load_data',
        mock_load()
    )
    actual = slow_dataset()
    assert expected == actual
