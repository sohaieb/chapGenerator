<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">ChapGenerator</h3>
  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/sohaieb/chapGenerator/issues">Report Bug</a>
    ·
    <a href="https://github.com/sohaieb/chapGenerator/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->

<strong>Table of Contents</strong>
<ol>
<li>
  <a href="#about-chapgenerator">About ChapGenerator</a>
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
<li><a href="#contributing">Contributing</a></li>
<li><a href="#license">License</a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#acknowledgments">Acknowledgments</a></li>
</ol>


<!-- ABOUT THE PROJECT -->

## About ChapGenerator

ChapGenerator is a python script that helps to include chapters into your MP4 videos. This will make markers for each
chapter which would be read by a video players supporting video chapters feature like: [MPC-HC](https://mpc-hc.org)
or [VLC](https://www.videolan.org/vlc/).

<img src="imgs\Screenshot_3.jpg"/>

### Built With

<img src="imgs/img2.png" width="150" height="50"/>  
<img src="imgs/img.png" width="150" height="50"/>

This script uses [FFMPEG](https://www.ffmpeg.org/download.html) executable bins by default, and developed by **Python3**.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites
1. Install last version of [Python](https://www.python.org/downloads/)
2. Copy/paste your input video into assets folder
3. In the `config.py` file, provide **only** these following necessary data:

```python
input_file_path = "test_video_input.mp4"  # your input file name
output_file_path = "test_video_output.mp4"  # your output file name
```
4. In the `assets/chapters.txt` provide your chapters & times accordingly
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage
Just execute the script by running: `python chapGenerator.py`
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

LinkedIn - [Sohaieb Azaiez](https://www.linkedin.com/in/azsoh)

Project Link: [https://github.com/sohaieb/chapGenerator](https://github.com/sohaieb/chapGenerator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>