# vocabulary_notebook
基于Python,pyqt5,excel,pyinstaller实现的单词记录本<br>
**requirement**:<br>
  python>=3.6
  pyqt5
  xlrd
  xlwt
  pyinstaller
<br>
界面简单，技术也不高深，就是解决实际问题（最近在刷TOEFL单词，想打造一款自己想要的单词记录软件），既然都花一晚上写出来了那就发到github上来保存着，以供交流学习。
<br>界面简陋如下：<br>
![Alt text](https://raw.githubusercontent.com/leviome/vocabulary_notebook/master/pictures/1.PNG)
<br>首先你有个生词本(excel)，记录着你老是记不住的单词，每当你遇到头疼模糊的单词就可以打开这个界面，输入你的单词，比如：<br>
![Alt text](https://raw.githubusercontent.com/leviome/vocabulary_notebook/master/pictures/2.PNG)
<br>这样就证明你原来的生词本中不存在这个词，那就把这个词添加到excel表格(生词本)。难道这个程序只能完成基础的增删查改？不存在的<br>
如果你输入的单词，存在于生词本(excel)中，那就会这样:<br>
![Alt text](https://raw.githubusercontent.com/leviome/vocabulary_notebook/master/pictures/3.PNG)
<br>其实当遇到的单词越来越多，我希望有一个软件能把我对单词的掌握程度做一个量化，就是输入这个软件的单词的重复次数，直接在excel表中呈现：<br>
![Alt text](https://raw.githubusercontent.com/leviome/vocabulary_notebook/master/pictures/4.PNG)
<br>上面就是生词本的截图，第一列代表单词，第二列代表我遗忘的次数。可以看到，已经有500多个单词了，在‘lust’的右边有一个数字‘3’，意思是，我记了3次都没记住。<br>
随着时间的推移，越来越多的单词将会加入，每个单词都会有或多或少的遗忘率，可以根据遗忘次数整理出自己比较虚的单词，加强记忆。
