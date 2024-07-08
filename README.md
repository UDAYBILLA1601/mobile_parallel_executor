# Mobile Test Automation with Parallel Execution

This project provides a framework for automating mobile tests with parallel execution support. It uses port assignment for connected devices, discovers connected mobiles, and runs tests in parallel.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Getting Started

Follow these instructions to set up and run the project on your local machine for development and testing purposes.

## Prerequisites

- Python 3.7+
- [ADB](https://developer.android.com/studio/command-line/adb) installed and configured for Android device discovery
- [psutil](https://pypi.org/project/psutil/) library for managing processes

## Installation

1. **Clone the repository:**

        git clone https://github.com/UDAYBILLA1601/mobile_parallel_executor
    cd your-repo-name
    

2. **Install the required Python packages:**

        pip install -r requirements.txt
    

## Usage

1. **Prepare your JSON test data file:**

    Create a JSON file (`test_data.json`) with the following structure:

        {
      "test_suit_1": [
        {
          "path": "test_cases.sample_record",
          "args": ["--test_config_root", "C:\\DummyPath\\Config", "--target_app", "dummy_app", "--polar_pattern", "\"Stereo\"", "--audio_format", "\"MP3 128 Kbps\"", "--audio_quality", "44.1KHZ", "--duration", "5.00"]
        },
        {
          "path": "test_cases.sample_record_long",
          "args": ["--test_config_root", "C:\\DummyPath\\Config", "--target_app", "dummy_app", "--polar_pattern", "\"Omnidirectional\"", "--audio_format", "\"WAV 256 Kbps\"", "--audio_quality", "48KHZ", "--duration", "10.00"]
        }
      ],
      "test_suit_2": [
        {
          "path": "test_cases.sample_test",
          "args": ["--test_config_root", "C:\\DummyPath\\Config", "--target_app", "dummy_app2"]
        }
      ]
    }
    

2. **Run the parallel executor:**

        python parallel_executor.py --test_suit_path path/to/test_data.json --target_app dummy_app
    

    This will parse the JSON file and handle the parallel execution of the test cases as specified.

## Project Structure

```plaintext
.
├── README.md
├── assignports.py
├── mobilesdiscover.py
├── parallel_executor.py
├── portscanner.py
├── test_sequence_parser.py
└── requirements.txt

└── requirements.txt
```


- **assignports.py**: Assigns ports to connected mobile devices.

- **mobilesdiscover.py**: Discovers connected Android and iOS devices.

- **parallel_executor.py**: Executes tests in parallel on connected devices.

- **portscanner.py**: Manages and checks the availability of network ports.

- **test_sequence_parser.py**: Parses test sequence data and prepares test execution commands.


## Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.

Create your feature branch (git checkout -b feature/your-feature-name).

Commit your changes (git commit -am 'Add some feature').

Push to the branch (git push origin feature/your-feature-name).

Create a new Pull Request.


## Author

Uday Billa - UDAYBILLA1601
## License

This project is licensed under the MIT License - see the LICENSE file for details.


markdown

### Steps to Follow:
1. **Place the `README.md`** file in the root directory of your repository.
2. **Ensure you have a `requirements.txt`** file listing all required Python packages.
3. **Include a sample JSON data file** for users to reference when creating their test data files.

Feel free to modify the content according to your project's specific needs.
