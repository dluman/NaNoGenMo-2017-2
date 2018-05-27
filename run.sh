count=0
while [ $count -le 50000 ]
do
	python main.py
	count=$(cat text.log | wc -w)
	echo $count
done
