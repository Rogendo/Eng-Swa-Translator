
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

<h3 align="center">English to Swahili Translator</h3>
<p align="center">Creating a model which will be able to translate English to Swahili using local datasets.</p>

  <p align="center">
   Revolutionzing Language Processing
    <br />
    <a href="https://github.com/Rogendo/Eng-Swa-Translator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Progress</a>
    ·
    <a href="#">Report Bug</a>
    ·
    <a href="https://github.com/Rogendo/Eng-Swa-Translator">Request Feature</a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![image](https://github.com/Rogendo/English-to-Swahili-Translation-NLP-/assets/62094358/302dfc8c-f6ed-4cbf-9b8f-65f56a660e9a)

#### 1.1 Problem Statement
The problem of translating English to Swahili presents several challenges, primarily due to the linguistic
differences between the two languages. Machine translation has made significant advancements, but there
is room for improvement in achieving accurate and contextually relevant translations. This project aims to
address these challenges and enhance the quality of English to Swahili translations using Natural
Language Processing (NLP) techniques.

#### 1.2 Objectives
The primary objectives of this project are as follows:
1. Develop a robust English-to-Swahili translation model: Create a machine translation model
capable of accurately translating English text into Swahili while preserving context and meaning.
2. Improve translation quality: Enhance the fluency, coherence, and accuracy of translated text to
make it more natural and contextually relevant for Swahili speakers.
3. Handle various text types and domains: Ensure the translation model can handle diverse text
types, including formal documents, informal conversations, technical content, and more.

#### 1.3 Project Structure
1. Dataset folder - All dataset csv should be placed there
2. Notebook folder - All notebook files should be placed there
3. Deployment folder - All Deployment should be placed there
4. Model folder - Any saved model should be placed there
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* <img width="12" /><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
* <img width="12" /><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="40" alt="flask logo"  />
* <img width="12" /><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="40" alt="git logo"  />


<p align="right">(<a href="#readme-top">back to top</a>)</p>

![Screenshot from 2024-01-24 11-14-42](https://github.com/Rogendo/Eng-Swa-Translator/assets/62094358/91b2ab82-77be-4784-9e42-e070c10dc4e4)


![Screenshot from 2024-01-07 11-41-01](https://github.com/Rogendo/Eng-Swa-Translator/assets/62094358/15807184-77d9-4bed-ad34-3c1c96199b2f)

# How to run it?

First step is to download the models from the link <a href="https://drive.google.com/drive/folders/1ybwgK1XNG1wd8As0m9vjMdQfHmD6E9uk?usp=sharing"> MODEL </a> add the model in the root project directory.

The following instructions were tested on the Windows and Linux with Python 3.8.

1. Clone this repository

```
git clone https://github.com/Rogendo/Eng-Swa-Translator.git
```
```
cd Eng-Swa-Translator/
```

2. Create and activate virtual environment 

```
python -m venv venv
```
on Linux system
```
source venv/bin/activate
```
on Windows system
```
.\venv\Scripts\activate.bat
```
3. Install requirements

```
pip install  -r requirements.txt
```

```
cd deployment/
```
4. Run the 
```
flask --app app --debug run

```
## Deployed Model on Hugging Face

The English-Swahili translation model has been successfully deployed on Hugging Face, a popular platform for hosting and sharing machine learning models. 
The deployment enables seamless integration with applications via an API, making it accessible to developers and end-users globally.

### Model Details

    Model Name: Rogendo/en-sw, Rogendo/sw-en
    Hosted Platform: Hugging Face Model Hub
    Architecture: Transformer-based Neural Network, fine-tuned for English-Swahili translations.
    Dataset: Trained on datasets like JW300 and CCMatrix, which include diverse linguistic contexts.

### How to Access the Model

    Visit the model's page on Hugging Face: [https://huggingface.co/Rogendo/en-sw](https://huggingface.co/Rogendo/en-sw).
    Use the Inference API directly from the Hugging Face interface:
        Input text in English or Swahili.
        Receive instant translations without additional setup.
    Integrate the model into your application:
        Install transformers via pip install transformers.
        Use the provided code snippet to load and use the model locally or through the API.

### Sample Code
``` python
"""
    main.py


    If training the model proves to be too much for you either computationally, or timewise, You can utilise the deployed version of the model in huggingface
    through the code provided below in the 'main.py' file  Example usage from the deployed model in huggingface. Happy coding! 
    
"""
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


eng_swa_tokenizer = AutoTokenizer.from_pretrained("Rogendo/en-sw")
eng_swa_model = AutoModelForSeq2SeqLM.from_pretrained("Rogendo/en-sw")

eng_swa_translator = pipeline(
    "text2text-generation",
    model = eng_swa_model,
    tokenizer = eng_swa_tokenizer,
)




swa_eng_tokenizer = AutoTokenizer.from_pretrained("Rogendo/sw-en")
swa_eng_model = AutoModelForSeq2SeqLM.from_pretrained("Rogendo/sw-en")

swa_eng_translator = pipeline(
    "text2text-generation",
    model = swa_eng_model,
    tokenizer = swa_eng_tokenizer,
)

def translate_text_swa_eng(text):
  translated_text = swa_eng_translator(text,max_length=128, num_beams=5)[0]['generated_text']
  return translated_text

def translate_text_eng_swa(text):
    translated_text = eng_swa_translator(text, max_length=128, num_beams=5)[0]['generated_text']
    return translated_text

text = "Ninampenda sana mama yangu, bila yeye singekuwa mahali nilipo sasa"
translate_text_swa_eng(text)

text = "My name is John, I love Food so much that I can let it kill me if it had hands of its own"
translate_text_eng_swa(text)


```

<!-- ROADMAP -->
## Roadmap

- [ ] Revolutionzing Language Processing


See the [open issues](https://github.com/Rogendo/Eng-Swa-Translator/issues/) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

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

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@Eng-swa-translator](https://twitter.com/@Eng-swa-translator) - 

Project Link: [https://github.com/Rogendo/Eng-Swa-Translator/issues](https://github.com/Rogendo/Eng-Swa-Translator/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Peter Rogendo](https://github.com/Rogendo/)
* [Kigen Chesire](https://github.com/kigenchesire/)
* [Frederick Kioko](https://github.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Rogendo/Eng-Swa-Translator.svg?style=for-the-badge
[contributors-url]: https://github.com/Rogendo/Eng-Swa-Translator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Rogendo/Eng-Swa-Translator.svg?style=for-the-badge
[forks-url]: https://github.com/Rogendo/Eng-Swa-Translator/network/members
[stars-shield]: https://img.shields.io/github/stars/Rogendo/Eng-Swa-Translator.svg?style=for-the-badge
[stars-url]: https://github.com/Rogendo/Eng-Swa-Translator/stargazers
[issues-shield]: https://img.shields.io/github/issues/Rogendo/Eng-Swa-Translator.svg?style=for-the-badge
[issues-url]: https://github.com/Rogendo/Eng-Swa-Translator/issues
[license-shield]: https://img.shields.io/github/license/Rogendo/Eng-Swa-Translator.svg?style=for-the-badge
[license-url]: https://github.com/Rogendo/Eng-Swa-Translator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/Discord-35495E?style=for-the-badge&logo=discord&logoColor=white
[linkedin-url]: #







