(ns fizzbuzz-clj.core
  (:gen-class))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (doseq [i (range 1 1000000001)]
    (let
      [fizz (= (mod i 3) 0)
       buzz (= (mod i 5) 0)]
      (->
        (cond
          (and fizz buzz) "Fizzbuzz!"
          fizz             "Fizz"
          buzz             "Buzz"
          :else             (format "%010d" i))
        (println)))))
