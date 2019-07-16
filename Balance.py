def printParenthesis(str, bs): 
	if(bs > 0): 
		_printParenthesis(str, 0,bs, 0, 0); 
	return; 

def _printParenthesis(str, pos, bs,open, close): 
	
	if(close == bs): 
		for i in str: 
			print(i, end = ""); 
		print(); 
		return; 
	else: 
		if(open > close): 
			str[pos] = '}'; 
			_printParenthesis(str, pos + 1, bs,open, close + 1); 
		if(open < bs): 
			str[pos] = '{'; 
			_printParenthesis(str, pos + 1, bs,open + 1, close); 


bs = int(input()); 
str = [""] * 2 * bs; 
printParenthesis(str, bs); 


