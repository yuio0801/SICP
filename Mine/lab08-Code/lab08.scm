;;; Lab08: Scheme

(define (over-or-under a b)
(
  if(< a b)
    -1
    (
      if(= a b)
        0
        1
    )
)  
)


(define (make-adder n)
  (define (adder x)
      (+ x n)
  )
  adder
)


(define (composed f g)
  (define (mix n)
    (f(g n))
  )
  mix
)


(define (remainder a b)
  (- a (* b (quotient a b))))

(define (gcd a b)
  (if(= b 0)
    a
    (gcd b (remainder a b))
  )
)


(define lst
  (list (list 1) 2 (list 3 4) 5)
)


(define (ordered s)
  (if(null? s)
    #t
    (if(null? (cdr s))
      #t
      (if( > (car s) (car (cdr s)))
        #f
        (ordered (cdr s))
      )
    )
  )
)
