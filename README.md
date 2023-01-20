<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/rockstarcoder333/Image2PSD">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Image2PSD</h3>

  <p align="center">
    PSD generation from scanned Document
    <br />
    <a href="https://github.com/rockstarcoder333/Image2PSD"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rockstarcoder333/Image2PSD">View Demo</a>
    ·
    <a href="https://github.com/rockstarcoder333/Image2PSD/issues">Report Bug</a>
    ·
    <a href="https://github.com/rockstarcoder333/Image2PSD/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/rockstarcoder333/Image2PSD)

This repository includes the code that generate PSD from scanned document.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Tensorflow][Tensorflow]][Tensorflow-url]
* [![Keras][Keras]][Keras-url]
* [![Numpy][Numpy]][Numpy-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* pip

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/rockstarcoder333/Image2PSD.git
   ```
2. Create venv and activate
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install packages
   ```sh
   cd Image-Processing-AI
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Generate PSD based on absolute position and font
 ```sh
 python drawPhotoshop_absolute.py
 ```

1. Generate PSD based on original position and font
 ```sh
 python drawPhotoshop_origin.py
 ```

_For more examples, please refer to the [Documentation](https://github.com/rockstarcoder333/Image2PSD)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links

See the [open issues](https://github.com/rockstarcoder333/Image2PSD/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

successcoder123@gmail.com

Project Link: [https://github.com/rockstarcoder333/Image2PSD](https://github.com/rockstarcoder333/Image2PSD)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
* [Photoshop api](https://github.com/loonghao/photoshop-python-api)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: images/result.jpg
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[TensorFlow]: https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/
[Keras]: https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white
[Keras-url]: https://keras.io/
[NumPy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/
