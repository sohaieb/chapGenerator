<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


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
  <a href="#about-chap-generator">About ChapGenerator</a>
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
<hr />

ChapGenerator is a python script that helps to include chapters into your MP4 videos. This will make markers for each
chapter which would be read by a video players supporting video chapters feature like: [MPC-HC](https://mpc-hc.org)
or [VLC](https://www.videolan.org/vlc/).

![Example of Generated chapters](.\imgs\Screenshot_3.jpg)

This script uses [FFMPEG](https://www.ffmpeg.org/download.html) executable bins by default.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How this works?

1. Install last version of [Python](https://www.python.org/downloads/)
2. Copy/paste your input video into assets folder
3. In the `config.py` file, provide **only** these following necessary data:

```python
input_file_path = "test_video_input.mp4"  # your input file name
output_file_path = "test_video_output.mp4"  # your output file name
```

4. In the `assets/chapters.txt` provide your chapters & times accordingly
5. Execute the script by: `python chapGenerator.py`

## Author

Sohaieb Azaiez

# Licence

![img.png](imgs/img.png)