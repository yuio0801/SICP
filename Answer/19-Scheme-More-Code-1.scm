(define (fact n)
	(if (= n 0)
		1
		(* n (fact (- n 1)))))

(define (fact2 n)
	(define (fact-tail n result)
		(if (<= n 1)
			result
			(fact-tail (- n 1) (* n result))))
	(fact-tail n 1))

(define (length2 lst)
	(define (length-tail lst len)
		(if (null? lst)
			len
			(length-tail (cdr lst) (+ 1 len))))
	(length-tail lst 0))


