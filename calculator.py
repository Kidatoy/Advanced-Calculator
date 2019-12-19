class Calculator(object):
  def eval(self, expression):

    expression = self.symbols(expression)

    if self.is_compound(expression):
      expression = self.simplify(expression)

    index = self.op_index(expression)
    if index is None:
      return [
        lambda: expression.replace('$','-'),
        lambda: float(expression)
      ][int(expression.isdigit())]()

    operation = expression[index]
    if operation == '-' and index == 0:
      expression = '$' + expression[1::]
      return self.eval(expression)

    lt_hand = expression[:index]
    rt_hand = expression[index+1::]
    
    if not lt_hand.isdigit():
      lt_hand = self.eval(lt_hand)
    if not rt_hand.isdigit(): 
      rt_hand = self.eval(rt_hand)
    calculation = self.compute(float(lt_hand), float(rt_hand), operation)

    if isinstance(calculation, str):
      calculation = float(calculation)
    
    return calculation

  def symbols(self, expression):
    if '+-' in expression: expression = expression.replace('+-','-')
    if '--' in expression: expression = expression.replace('--','+')
    if '*-' in expression: expression = expression.replace('*-','*$')
    if '/-' in expression: expression = expression.replace('/-','/$')
    if '^-' in expression: expression = expression.replace('^-','^$')
    if 'pi' in expression: expression = expression.replace('pi','3.1415926535')

    return expression

  def op_index(self, expression):
    if '-' in expression: return expression.index('-')
    if '+' in expression: return expression.index('+')
    if '/' in expression: return expression.index('/')
    if '*' in expression: return expression.index('*')
    if '^' in expression: return expression.index('^')

    return None

  def compute(self, exp1, exp2, operation):
    return {
      '-': lambda: exp1 - exp2,
      '+': lambda: exp1 + exp2,
      '/': lambda: exp1 / exp2,
      '*': lambda: exp1 * exp2,
      '^': lambda: exp1 ** exp2
    }[operation]()
  
  def prompt(self):
    return self.eval(input("Enter a mathmatical expression: "))
  
  def substr(self, expression):
    i = expression.find('(')
    j = expression.rfind(')')

    return i, j
  
  def simplify(self, expression):
    start, stop = self.substr(expression)
    substr = expression[start:stop+1]
    newstr = str(self.eval(expression[start+1: stop]))
   
    return expression.replace(substr, newstr)

  def is_compound(self, expression):
    return '(' in expression
