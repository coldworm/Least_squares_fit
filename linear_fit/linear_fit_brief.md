参考链接：https://www.cnblogs.com/code-juggler/p/8406449.html  
  
设采样值（实际值，**观察值**）(x<sub>i</sub>, y<sub>i</sub>)，其中i=1,2,3......n  
  ![]()
回归直线方程:
![](https://latex.codecogs.com/svg.latex?\hat{y}%20=%20a%20+%20bx)，![](https://latex.codecogs.com/svg.latex?\hat{y})为近似值  
我们希望所有的近似值和观察值的偏差尽量小，由于平方又称二乘方，所以这种“离差平方和为最小”的方法，称为：**最小二乘法**。
![](https://latex.codecogs.com/svg.latex?Q%20=%20\sum_{i=1}^{n}(y_i-\hat{y_i})^2%20=%20\sum_{i=1}^{n}(y_i-a-bx_i)^2)  
解得：  
![](https://latex.codecogs.com/svg.latex?\hat{b}%20=%20\frac{%20\sum_{i=1}^{n}x_iy_i-n\bar{x}\bar{y}}{\sum_{i=1}^nx_i^2-n\bar{x}^2)  
![](https://latex.codecogs.com/svg.latex?\hat{a}%20=%20\bar{y}%20-%20\hat{b}\bar{x})  
  
推导，需要使用两个公式，  
(1)![](https://latex.codecogs.com/svg.latex?\sum_{i=1}^{n}(x_i-\bar{x})^2=\sum_{i=1}^{n}x_i^2-n\bar{x}^2),其中![](https://latex.codecogs.com/svg.latex?\bar{x}=\frac{x_1+x_2+x_3+\cdots+x_n}{n})为x_i的均值  
证明：  
![](https://latex.codecogs.com/svg.latex?\sum_{i=1}^{n}(x_i-\bar{x})^2=(x_1-\bar{x})^2+(x_2-\bar{x})^2+\cdots+(x_n-\bar{x})^2)  
![](https://latex.codecogs.com/svg.latex?=(x_1^2-2x_1\bar{x}+\bar{x}^2)+(x_2^2-2x_2\bar{x}+\bar{x}^2)+\cdots+(x_n^2-2x_n\bar{x}+\bar{x}^2))  
![](https://latex.codecogs.com/svg.latex?=(x_1^2+x_2^2+\cdots+x_n^2)+n\bar{x}^2-2\bar{x}(x_1+x_2+\cdots+x_n))  
![](https://latex.codecogs.com/svg.latex?=\sum_{i=1}^{n}x_i^2+n\bar{x}^2-2*\bar{x}*n*\frac{(x_1+x_2+\cdots+x_n)}{n})  
![](https://latex.codecogs.com/svg.latex?=\sum_{i=1}^{n}x_i^2+n\bar{x}^2-2n\bar{x}^2)  
![](https://latex.codecogs.com/svg.latex?=\sum_{i=1}^{n}x_i^2-n\bar{x}^2)  
  
(2)![](https://latex.codecogs.com/svg.latex?\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})=\sum_{i=1}^{n}x_iy_i-n\bar{x}\bar{y})  
证明：  
![](https://latex.codecogs.com/svg.latex?\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})=(x_1-\bar{x})(y_1-\bar{y})+(x_2-\bar{x})(y_2-\bar{y})+\cdots+(x_n-\bar{x})(y_n-\bar{y}))  
![](https://latex.codecogs.com/svg.latex?=(x_1y_1+\bar{x}\bar{y}-x_1\bar{y}-y_1\bar{x})+(x_2y_2+\bar{x}\bar{y}-x_2\bar{y}-y_2\bar{x})+\cdots+(x_ny_n+\bar{x}\bar{y}-x_n\bar{y}-y_n\bar{x}))  
![](https://latex.codecogs.com/svg.latex?=\sum_{i=1}^{n}x_iy_i+n*\bar{x}\bar{y}-n*\bar{y}*\frac{(x_1+x_2+\cdots+x_n)}{n}-n*\bar{x}*\frac{(y_1+y_2+\cdots+y_n)}{n})  
![](https://latex.codecogs.com/svg.latex?=\sum_{i=1}^{n}x_iy_i-n\bar{x}\bar{y})  
  
最小二乘法求回归直线方程公式推导  
![](https://latex.codecogs.com/svg.latex?Q=\sum_{i=1}^{n}(y_i-a-bx_i)^2)  
![](https://latex.codecogs.com/svg.latex?=(y_1-a-bx_1)^2+(y_2-a-bx_2)^2+\cdots+(y_n-a-bx_n)^2)  
![](https://latex.codecogs.com/svg.latex?=(y_1^2+a^2+b^2x_1^2+2abx_1-2ay_1-2bx_1y_1)+\cdots+(y_n^2+a^2+b^2x_n^2+2abx_n-2ay_n-2bx_ny_n))  
![](https://latex.codecogs.com/svg.latex?=\sum_{i=1}^{n}y_i^2+na^2+b^2\sum_{i=1}^{n}x_i^2+n*2ab*\frac{(x_1+x_2+\cdots+x_n)}{n}-n*2a*\frac{(y_1+y_2+\cdots+y_n)}{n}-2b\sum_{i=1}^{n}x_iy_i)  
![](https://latex.codecogs.com/svg.latex?=\sum_{i=1}^{n}y_i^2+na^2+b^2\sum_{i=1}^{n}x_i^2+2nab\bar{x}-2na\bar{y}-2b\sum_{i=1}^{n}x_iy_i)  
![](https://latex.codecogs.com/svg.latex?=\sum_{i=1}^{n}y_i^2-2b\sum_{i=1}^{n}x_iy_i+b^2\sum_{i=1}^{n}x_i^2+na^2-2na(\bar{y}-b\bar{x}))  
![](https://latex.codecogs.com/svg.latex?=\sum_{i=1}^{n}y_i^2-2b\sum_{i=1}^{n}x_iy_i+b^2\sum_{i=1}^{n}x_i^2+n(a-(\bar{y}-b\bar{x}))^2-n(\bar{y}-b\bar{x})^2)  
![](https://latex.codecogs.com/svg.latex?=\sum_{i=1}^{n}y_i^2-2b\sum_{i=1}^{n}x_iy_i+b^2\sum_{i=1}^{n}x_i^2+n(a-(\bar{y}-b\bar{x}))^2-n\bar{y}^2+2nb\bar{x}\bar{y}-nb^2\bar{x}^2)  
![](https://latex.codecogs.com/svg.latex?=n(a-(\bar{y}-b\bar{x}))^2+b^2(\sum_{i=1}^{n}x_i^2-n\bar{x}^2)-2b(\sum_{i=1}^{n}x_iy_i-n\bar{x}\bar{y})+(\sum_{i=1}^{n}y_i^2-n\bar{y}^2))  
  
为了使上式的值最小，需要：  
![](https://latex.codecogs.com/svg.latex?n(a-(\bar{y}-b\bar{x}))^2=0)，且![](https://latex.codecogs.com/svg.latex?b^2(\sum_{i=1}^{n}x_i^2-n\bar{x}^2)-2b(\sum_{i=1}^{n}x_iy_i-n\bar{x}\bar{y})+(\sum_{i=1}^{n}y_i^2-n\bar{y}^2))取最小值，抛物线，b取对称轴时代数式取值最小，即：  
![](https://latex.codecogs.com/svg.latex?b=\frac{\sum_{i=1}^{n}x_iy_i-n\bar{x}\bar{y}}{\sum_{i=1}^{n}x_i^2-n\bar{x}^2}=\frac{n(\sum_{i=1}^{n}x_iy_i)-(\sum_{i=1}^{n}x_i)(\sum_{i=1}^{n}y_i)}{n(\sum_{i=1}^{n}x_i^2)-(\sum_{i=1}^{n}x_i)^2})  
![](https://latex.codecogs.com/svg.latex?a=\bar{y}-b\bar{x}=\frac{(\sum_{i=1}^{n}x_i^2)(\sum_{i=1}^{n}y_i)-(\sum_{i=1}^{n}x_i)(\sum_{i=1}^{n}x_iy_i)}{n(\sum_{i=1}^{n}x_i^2)-(\sum_{i=1}^{n}x_i)^2})  

