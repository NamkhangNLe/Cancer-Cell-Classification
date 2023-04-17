# Cancer-Cell-Classification
This is a Python program that takes in a color photo of cancer cells and converts it to a black and white image using Hough Transform. 
A popular technique used in computer vision and image processing for detecting lines, curves, and shapes in an image. 
It is a mathematical technique that transforms the points in the image space to the parameter space, where the shapes are represented in a parametric form.
The basic idea behind Hough Transform is to consider each point in the image space as a potential part of a shape,
and then find the parameters of the shape that the point belongs to. For instance, in the case of detecting lines,
each point in the image space represents a point on a line, and the parameters of the line can be represented using the slope and the intercept.
To perform Hough Transform, a voting process is used to accumulate the parameters of the shape for each point in the image space.
In the case of detecting lines, for each point in the image space, a set of lines is generated that pass through the point,
and the corresponding parameters of the lines are voted for in the parameter space.
The parameter space is typically represented as an accumulator array, where each element represents a particular combination of the parameters.
Once the voting process is complete, the elements of the accumulator array that receive the most votes correspond to the parameters of the shapes in the image space.
In the case of detecting lines, the peaks in the accumulator array represent the parameters of the lines in the image space.
One of the major advantages of Hough Transform is that it is robust to noise and can handle incomplete shapes.
However, it is computationally expensive and can be sensitive to the choice of parameters.
Additionally, it may require fine-tuning for different types of shapes and images.
