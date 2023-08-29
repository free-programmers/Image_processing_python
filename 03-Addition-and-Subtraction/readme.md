Addition of Image:
We can add two images by using function cv2.add(). This directly adds up image pixels in the two images. 
 

Syntax: cv2.add(img1, img2)
But adding the pixels is not an ideal situation. So, we use cv2.addweighted(). Remember, both images should be of equal size and depth. 
 

Syntax: cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)
```md
        Parameters: 
        img1: First Input Image array(Single-channel, 8-bit or floating-point) 
        wt1: Weight of the first input image elements to be applied to the final image 
        img2: Second Input Image array(Single-channel, 8-bit or floating-point) 
        wt2: Weight of the second input image elements to be applied to the final image 
        gammaValue: Measurement of light

```
 


https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-1-addition-and-subtraction/