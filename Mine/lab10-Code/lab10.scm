;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (if (null? s) 
      nil
      (if (f (car s))
          (cons-stream (car s) (filter-stream f (cdr-stream s)))
          (filter-stream f (cdr-stream s))
      )
  )
)


(define (slice s start end)
  (define (helper s start end pos)
    (if (null? s)
        nil
        (if (= pos end)
            nil
            (if (or (= pos start) (> pos start))
              (cons (car s) (helper (cdr-stream s) start end (+ 1 pos)))
              (helper (cdr-stream s) start end (+ 1 pos))
            )
        )
    )
  )
  (helper s start end 0)
)


(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define factorials
  (cons-stream 1 (combine-with * (naturals 1) factorials))
)


(define fibs
  (cons-stream
    0
    (cons-stream 1 (combine-with + fibs (cdr-stream fibs)))
  )
)


(define (exp x)
  (define inx (cons-stream x inx) )
  (cons-stream 1 (combine-with + (exp x) (combine-with / (combine-with expt inx (naturals 1)) (cdr-stream factorials) ) ))
)

(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))


(define (nondecrease s)
  (define (helper s tmp last)
    (if (null? s)
        (if (null? tmp)
            nil
            (cons-stream tmp nil)
        )
        (if (or (= (car s) last) (> (car s) last) )
            (helper (cdr-stream s) (append tmp (list (car s))) (car s) )
            (cons-stream tmp (helper (cdr-stream s) (list (car s)) (car s)) )
        )
    )
  )
  (helper s nil -1)
)


;;; Just For Fun Problems

(define (my-cons-stream first second) ; Does this line need to be changed?
  'YOUR-CODE-HERE
)

(define (my-car stream)
  'YOUR-CODE-HERE
)

(define (my-cdr-stream stream)
  'YOUR-CODE-HERE
)


(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes (sieve (naturals 2)))
