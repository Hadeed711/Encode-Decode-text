# EncText Encoding and Decoding
Overview
This Python script provides functionality for encoding and decoding text. The encoding process transforms words longer than three characters by appending random characters and rearranging their letters, while shorter words are reversed. The decoding process reverses the encoding steps, restoring the original text.

Features
Encoding Functionality:
Transforms words longer than three characters by:
Moving the first character to the end of the word.
Adding three random alphabetic characters before and after the modified word.
Reverses words that are three characters or shorter.
Decoding Functionality:
Reverts the encoding process, reconstructing the original text from the encoded string.
How It Works
Encoding:

The encode_language function splits the input text into words and processes each word:
For words longer than three characters:
The first character is moved to the end.
Three random alphabetic characters are generated and added before and after the modified word.
Words three characters or shorter are reversed.
The modified words are then joined to form the encoded text.
Decoding:

The decode_language function splits the encoded text back into words and processes each word:
For words longer than six characters (which include random characters):
The random characters are removed, and the last character of the remaining string (original first character) is placed back at the start.
Shorter words are reversed back to their original form.
The processed words are joined to recreate the original text.
Usage
To use the script:

Clone the repository or download the script.
Run the script in a Python environment.
Enter the text you want to encode when prompted.
The encoded text will be displayed, followed by the decoded text, which should match the original input.
