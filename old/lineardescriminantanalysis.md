# Linear Descriminant Analysis
* [from this](https://www.python-course.eu/linear_discriminant_analysis.php)
* **Between Class Scatter** = Sb
* **Within Class Scatter** = Sw
* Linear Descriminant Analysis searches for a projection of dataset *A*, that maximizes the Sb/Sw ratio.
* The goal is to project / transform dataset *A* using a transformation matrix *w* such that the ratio between class between scatter (*Sb*) and within class scatter (*Sw*) is maximized.

* The transformed dataset is 
$$
Y = A * w^t
$$

## What is *Scatter Within*
* $$S_W$$

## What is *Scatter Between*
* $$S_B$$

## How to do the transformation
* We know that we want to minimize $$\frac{S_B}{S_W}$$
* And we want to transform this like
$$ Y = w^T * X $$
