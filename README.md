**Фантазери**  
Борби Антін та Орі придумали гру - вигадувати випадкові двійкові числа, і перевіряти, чи ці числа можна розбити на шматки, кожен з яких є степенем числа X у десятковій системі.  

Наприклад, якщо X == 5, то двійкове число число 101110011 можна розбити на 101, 11001 та 1, кожне з яких є 5 у якомусь степені (101 у десятковій == 5 == 5^1, 11001 == 25 == 5^2 та 1 == 1 - це 5^0).  

Продемонструйте, що люди розумніші за бобрів, і для заданого двійкового числа N знайдіть найменшу кількість шматків, на які його треба розбивати.  

**Вхідні дані:**  
	Перший рядок містить X - послідовність нуликів та одиничок та N.  

**Вихідні дані:**  
	Найменша кількість шматків, на які можемо розбити вхідне число, або -1 якщо це не можливо.  

**Обмеження:**  
	0 < len(X) < 100  
	0 < N < 100  
	
**Algorithm description**  
1. Filling list with powers of given decimal number and reversing it, so the biggest power will go first  
2. Taking powers one by one from our list, comparing them to our binary number, if it fits: counting how many times we can replace them. Memorizing binary number after replacement and comparing last numbers of binary number after replacement and before (because last number of odd binary powers will always be 1) so we can't take wrong power.  
3. After all the comparisons replacing binary number with memorized binary number after replacement and memorizing sum of replaces before step 2 and replaces made in step 2.  
4. Repeating step 2 untill we are finished and checking if binary number or replaces count exists before returning our replaces count as a result.  

  **To run my code:**  
• Download/clone this repository  
• Use command in folder which contains main.py: ```python3 main.py``` (could be "py" or "python" depending on your python version)  
• To launch doctests using console type: ```python3 -m unittest test_fantz.py``` (in the same folder as step before) 
