参考链接：https://wenku.baidu.com/view/ecda32525beef8c75fbfc77da26925c52dc59156.html  
**公式推导**  
二维平面圆方程表达式：  
![](https://latex.codecogs.com/svg.latex?(x-x_0)^2%20+%20(y-y_0)^2%20=%20r^2%20\quad\quad\quad\quad(1))  
最小二乘法的圆拟合，其误差平方的优化目标函数为：  
![](https://latex.codecogs.com/svg.latex?S%20=%20\sum_{i=1}^{n}[\sqrt{(x_i-x_0)^2+(y_i-y_0)^2}-r]^2)  
为避免平方根，优化目标函数如下：  
![](https://latex.codecogs.com/svg.latex?E%20=%20\sum_{i=1}^{n}[(x_i-x_0)^2+(y_i-y_0)^2-r^2]^2%20\quad\quad\quad\quad(2))  
![](https://latex.codecogs.com/svg.latex?E%20=%20\sum_{i=1}^{n}(x_i^2-2x_0x_i+x_0^2+y_i^2-2y_0y_i+y_0^2)^2%20\quad(3))  
令 ![](https://latex.codecogs.com/svg.latex?A=-2x_0)，![](https://latex.codecogs.com/svg.latex?B=-2y_0)，![](https://latex.codecogs.com/svg.latex?C=x_0^2+y_0^2-r^2)  
![](https://latex.codecogs.com/svg.latex?E%20=%20\sum_{i=1}^{n}(x_i^2+y_i^2+Ax_i+By_i+C)^2)  
由最小二乘法原理，参数A、B、C应使得E取极小值。根据极小值的求法，A、B和C应满足：  
![](https://latex.codecogs.com/svg.latex?\frac{\partial{E}}{\partial{A}}%20=%202\sum_{i=1}^{n}(x_i^2+y_i^2+Ax_i+By_i+C)x_i%20=%200%20\quad%20(4))  
![](https://latex.codecogs.com/svg.latex?\frac{\partial{E}}{\partial{B}}%20=%202\sum_{i=1}^{n}(x_i^2+y_i^2+Ax_i+By_i+C)y_i%20=%200%20\quad%20(5))  
![](https://latex.codecogs.com/svg.latex?\frac{\partial{E}}{\partial{C}}%20=%202\sum_{i=1}^{n}(x_i^2+y_i^2+Ax_i+By_i+C)%20=%200%20\quad\quad%20(6))  
求解方程组，先消去C，因为 ![](https://latex.codecogs.com/svg.latex?\sum_{i=1}^{n}Cx_i=C\sum_{i=1}^{n}x_i)，![](https://latex.codecogs.com/svg.latex?\sum_{i=1}^{n}C=nC)  
则式(4)\*n-(6)\*![](https://latex.codecogs.com/svg.latex?\sum_{i=1}^{n}x_i)得：  
![](https://latex.codecogs.com/svg.latex?\left(n\sum_{i=1}^{n}x_i^2-\sum_{i=1}^{n}x_i\sum_{i=1}^{n}x_i\right)A+\left(n\sum_{i=1}^{n}x_iyi-\sum_{i=1}^{n}x_i\sum_{i=1}^{n}y_i\right)B+n\sum_{i=1}^{n}x_i^3+n\sum_{i=1}^{n}x_iy_i^2-\sum_{i=1}^{n}(x_i^2+y_i^2)\sum_{i=1}^{n}x_i=0%20\quad%20(7))  
式(5)\*n-(6)\*![](https://latex.codecogs.com/svg.latex?\sum_{i=1}^{n}y_i)得：  
![](https://latex.codecogs.com/svg.latex?\left(n\sum_{i=1}^{n}x_iy_i-\sum_{i=1}^{n}x_i\sum_{i=1}^{n}y_i\right)A+\left(n\sum_{i=1}^{n}yi^2-\sum_{i=1}^{n}y_i\sum_{i=1}^{n}y_i\right)B+n\sum_{i=1}^{n}y_i^3+n\sum_{i=1}^{n}x_i^2y_i-\sum_{i=1}^{n}(x_i^2+y_i^2)\sum_{i=1}^{n}y_i=0%20\quad(8))  
令![](https://latex.codecogs.com/svg.latex?M_{11}=\left(n\sum_{i=1}^{n}x_i^2-\sum_{i=1}^{n}x_i\sum_{i=1}^{n}x_i\right)%20\quad\quad\quad\quad\quad\quad%20(9))  
![](https://latex.codecogs.com/svg.latex?M_{12}=M_{21}=\left(n\sum_{i=1}^{n}x_iyi-\sum_{i=1}^{n}x_i\sum_{i=1}^{n}y_i\right)%20\quad\quad\quad%20(10))  
![](https://latex.codecogs.com/svg.latex?M_{22}=\left(n\sum_{i=1}^{n}yi^2-\sum_{i=1}^{n}y_i\sum_{i=1}^{n}y_i\right)%20\quad\quad\quad\quad\quad\quad\quad%20(11))  
![](https://latex.codecogs.com/svg.latex?H_1=n\sum_{i=1}^{n}x_i^3+n\sum_{i=1}^{n}x_iy_i^2-\sum_{i=1}^{n}(x_i^2+y_i^2)\sum_{i=1}^{n}x_i%20\quad%20(12))  
![](https://latex.codecogs.com/svg.latex?H_2=n\sum_{i=1}^{n}y_i^3+n\sum_{i=1}^{n}x_i^2y_i-\sum_{i=1}^{n}(x_i^2+y_i^2)\sum_{i=1}^{n}y_i%20\quad%20(13))  
将(7),(8)式写成矩阵形式：  
![](https://latex.codecogs.com/svg.latex?\left[%20\begin{matrix}%20%20%20M_{11}%20&%20M_{12}%20%20\\\\%20%20%20M_{21}%20&%20M_{22}%20%20\\%20%20\end{matrix}\right]\left[%20\begin{matrix}%20%20%20A%20%20\\\\%20%20%20B%20%20\\%20%20\end{matrix}\right]=\left[%20\begin{matrix}%20%20%20-H_1%20%20\\\\%20%20%20-H_2%20%20\\%20%20\end{matrix}\right]%20\quad\quad%20(14))  
根据式(14),(6) 可得：  
![](https://latex.codecogs.com/svg.latex?A=\frac{H_2M_{12}-H_1M_{22}}{M_{11}M_{22}-M_{12}M_{21}})  
![](https://latex.codecogs.com/svg.latex?B=\frac{H_2M_{11}-H_1M_{21}}{M_{12}M_{22}-M_{11}M_{22}})  
![](https://latex.codecogs.com/svg.latex?C=-\frac{\sum_{i=1}^{n}(x_i^2+y_i^2+Ax_i+By_i)}{n})  
得到最佳拟合圆心坐标(x0,y0)，半径r的拟合值：  
![](https://latex.codecogs.com/svg.latex?x_0=-\frac{A}{2},y_0=-\frac{B}{2},r=\frac{1}{2}\sqrt{A^2+B^2-4C})  
