;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (make-change total biggest)
  (define (helper total biggest ans tmp)
    (if (= total 0)
        (if (null? ans)
            (list tmp)
            (list ans tmp)
        )
        (if (< total biggest)
            (helper total total ans tmp)
            (if (> biggest 1)
              (append 
                      (append ans
                              (helper (- total biggest) biggest ans (append tmp (list biggest)))
                      ) 
                      (helper total (- biggest 1) ans tmp)
              )
              (append ans 
                      (helper (- total biggest) biggest ans (append tmp (list biggest))) 
              )
            )
        )
    )
  )
  (helper total biggest nil nil)
)

(define (find n lst)
  (define (helper n lst rank)
    (if (= n (car lst))
        rank
        (helper n (cdr lst) (+ 1 rank))
    )
  )
  (helper n lst 0)
)

(define (printpath lst sym)
  (if (null? lst)
      sym
      (if (= (car lst) 0)
          `(car ,(printpath (cdr lst) sym))
          `(cdr ,(printpath (cdr lst) sym))
      )
  )
)

(define (find-nest n sym)
  (define (helper n sym lst tmp)
    (if (null? lst)
        nil
        (if (number? (car lst))
            (if (= (car lst) n)
                (printpath (append '(0) tmp) sym)
                (helper n sym (cdr lst) (append '(1) tmp))
            )
            (append
              (helper n sym (car lst) (append '(0) tmp))
              (helper n sym (cdr lst) (append '(1) tmp))
            )
        )
    )
  )
  (helper n sym (eval sym) nil)
)


(define-macro (my/or operands)
  (cond
    ((null? operands) #f)
    ((null? (cdr operands)) (car operands))
    (else
      `(let ((t ,(car operands)))
        (if t
            t 
            (my/or ,(cdr operands))
        )
      )
    )
  )
)
(define-macro (my/and operands)
  (cond 
    ((null? operands) #t)
    ((null? (cdr operands)) (car operands))
    (else
      `(let ((t ,(car operands)))
         (if t
             (my/and ,(cdr operands))
             #f)))))

(define (remove args vals indices pos ans)
  (if (null? indices)
      (append ans args)
      (if (=  pos (car indices))
          (remove (cdr args) (cdr vals) (cdr indices) (+ 1 pos) (append ans (list (car vals))))
          (remove (cdr args) vals indices (+ 1 pos) (append ans (list (car args))))
      )
  )
)
(define (removenum args ans)
  (if (null? args)
      ans
      (if (number? (car args))
          (removenum (cdr args) ans)
          (removenum (cdr args) (append ans (list (car args))))
      )
  )
)
(define-macro (myq lst)
  `(quote ,lst)
)

(define (dhelper fn args vals)
  (eval `(define ,(append '(g) args)
          ,(append (list fn) vals)
          )
  )
  g
)

(define-macro (k-curry fn args vals indices)
  `(dhelper (myq ,fn) (myq ,(removenum (remove args vals indices 0 nil) nil)) (myq ,(remove args vals indices 0 nil)) )
)


(define-macro (let* bindings expr)
  (if (null? bindings)
        `(let () ,expr)
        `(let (,(car bindings)) (let* ,(cdr bindings) ,expr))
  )
)

;;; Just For Fun Problems


; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  'YOUR-CODE-HERE
)


; only testing if your code could expand to a valid expression 
; resulting in my/and/2 and my/or/2 not hygienic
(define (gen-sym) 'sdaf-123jasf/a123)

; in these two functions you can use gen-sym function.
; assumption:
; 1. scm> (eq? (gen-sym) (gen-sym))
;    #f
; 2. all symbol generate by (gen-sym) will not in the source code before macro expansion
(define-macro (my/and/2 operands)
  'YOUR-CODE-HERE
)

(define-macro (my/or/2 operands)
  'YOUR-CODE-HERE
)