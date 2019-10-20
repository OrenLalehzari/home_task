import subprocess

MEDIA_FILES_URL = 'tests/images/image_to_process'
COMMAND_FUNCTION = 'image-processing/main.py'


def image_processing_module():
    results_list = None
    try:
        results = subprocess.check_output(['python3.6', COMMAND_FUNCTION, MEDIA_FILES_URL])
        results_list = eval(results)
    except:
        pass
    assert type(results_list) is list, 'Should be list'


if __name__ == "__main__":
    image_processing_module()
    print("Everything passed")
