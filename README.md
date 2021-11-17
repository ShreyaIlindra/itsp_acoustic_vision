# TEAM : Acoustic Vision
1. Shreya Ilindra 
2. Sai Aneesh Suryadevara
3. N Sai Gangadhar
4. V Indrahas Reddy

## Image to Speech Converter for Visually Impaired | ITSP
Worked in a team of four on an Institute Technical Summer Project (ITSP)

• Built a Convolutional Neural Network using TensorFlow, trained it to identify the text

• Implemented (MSER) algorithm to extract text from an image in an unstructured environment

• Included a Tesseract OCR model for images in structured environment to improve accuracy

• Used a Text-to-Speech (TTS) module to read the identified text out aloud and guide the user

<hr/>
Here we divided the task of text detection into two parts. 

## Case (1):Books / Documents
One for text identification in structured environments, say when we are reading books or documents. Here we have directly implemented the tesseract OCR module (pytesseract) for text identification. Then we pass it to the TTS module for reading out loud. (gtts)

## Case(2): Natural Scene text detection
Now for unstructured environments, which is the case we are primarily solving for, we have to read out text from everyday billboards and shop signs etc.
For this task, we have to first obtain the Bounding Boxes around each letter-  

### Method 1: MSER

#### Step 1: Detect Candidate Text Regions Using MSER (blob detection)
Finding Maximally Stable Extremal Region MSER is used to get the outline of the text in a proper form and to avoid the broken or non-uniform alignment of pixels. The word extremal refers to the property that all pixels inside the MSER have either higher (bright extremal regions) or lower (dark extremal regions) intensity than all the pixels on its outer boundary

#### Step 2: Remove Non-Text Regions Based On Basic Geometric Properties
Using MSER, connected component regions are detected. Geometric properties are used to filter out non-text region using threshold. Some of the geometric properties that are used in this system include: 

* Eccentricity: It is used to count the circular nature of the given regions. 
* Solidity: It is the proportion of the pixels in the raised structure area that are likewise in a given region. It is calculated by, Area / raised area 
* Extent: The location and size of the rectangle. 
* Euler Number: It is a feature of the binary image. 

#### Step 3: Remove Non-Text Regions Based On Stroke Width Variation
It is based on the fact that text in adjacent regions roughly have the same stroke width.

### Method 2 : EAST 
Instead of this lengthy process by MSER we can use an alternative. This approach is using a deep learning-based text detector called EAST, which is based on Zhou et al.’s 2017 paper, EAST: An Efficient and Accurate Scene Text Detector.

### CNN PART
Next we pass these bounding boxes  into the CNN for identifying for identifying each letter/number. We have trained a convolutional neural network for the same in TensorFlow.
* Custom dataset, containing 62  categories = 10 numbers + 26 letters + 26 capital letters
* Input image size for CNN is 64x64x3.
* 2 hidden layers using relu activation and dropout (for regularization effect)
* Loss function used is softmax_cross_entropy_with_logits()
* Mini-batch gradient descent is used.

Now save the trained model “my-test-model” and use it for prediction.

After prediction all the identified letters are concatenated and passed to the TTS module which reads it aloud.
