# model-mirror

This repo is for the Model in the Mirror project that ran from July 20th to August 25th, 2023. The purpose of this project was to create a Python script that would take an input text, create machine generated text via an LLM, and use an NLP to create a C-test for language learning purposes. The main files within this repo are newgenerator.py, which is the passage generator, any one of the spacy files, which can be used to create the c-tests from a passage input, and the database files where the passages are stored. Overall, the project was a success, but there is much refinement and new angles that can be explored with more time and research (i.e. creating a direct pipeline from database to c-test generation, improving the c-test to exclude certain types of tokens).

# But Wait! There's More!

After the project runtime was finished, there has been more work done as a result of me (Zeb) being rehired (hooray!).

# What's New
## pipeline.py

This is the direct pipeline from database to c-test generation.

## spacyfunctions.py

The spacy functions (and most other functions not directly related to prompt generation) are all stored within this file.

Some updates:
<ul>
    <li>
    testGen is the new primary generator. It's fully paramaterized and can exclude certain tokens from being gapped according to certain attributes. In summary: 
    <ol>
        <li>Token Length!</li>
        <li>Token Type!</li>
        <li>Token Frequency!</li>
        <li>Parts of Speech Included (Y/N)</li>
    </ol>
    </li>
    <li>Can now print 3 versions of the C-test to terminal, file, or directly to H5P content file.</li>
    <li>A bunch of language-specific functions for simplicity's sake.</li>
    <li>IN PROGRESS: Full-word gapping</li>
</ul>