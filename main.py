def pattern(n)
 if n <=0
    return ""
    elsif n == 1
      return "1"
      else
      length = (2*n)-1
      f_half =(1..n).map do |x|
              nums= 1. upto(x). map{|k| k%10}