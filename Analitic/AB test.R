library(DescTools)
library(ggplot2)

boostrap <- function(control, test, N) {
  set.seed(123)
  P_old <- mean(control)
  P_new <- mean(test)
  
  diff <- P_new - P_old
  
  differences <- rep(NA, N) 
  for(i in 1:N){
    s1 <- sample(control, replace = TRUE)
    s2 <- sample(test, replace = TRUE)
    p1 <- sum(s1)/length(s1)
    p2 <- sum(s2)/length(s2)
    p_diff <- p2 - p1 
    differences[i] <- p_diff
  }
  
  differences_cent <- differences - mean(differences)
  P_value <- sum(differences_cent > diff)
  return(list(differences, P_value))
}

df <- read.csv(file.choose())

test_group <- df[df$Variant == "10", ]
control_group <- df[df$Variant == "90", ]

test_cnt <- test_group$cnt.addToCart.
test_sum <- test_group$sum.addToCartItems.
control_cnt <- control_group$cnt.addToCart.
control_sum <- control_group$sum.addToCartItems.

par(mfrow = c(1, 2))
plot(test_cnt, test_sum,
     xlab = "Кол-во товара в корзине",
     ylab = "Сумма товара в корзине ",
     xlim = c(10, 200),
     ylim = c(0, 300000),
     main = "Калькулятор размеров",
     col = "blue",
     pch = 20)
plot(control_cnt, control_sum,
     xlab = "Кол-во товара в корзине",
     ylab = "Сумма товара в корзине ",
     xlim = c(10, 200),
     ylim = c(0, 300000),
     main = "Таблица размеров",
     col = "red",
     pch = 20)

# из приведенных выше графиков видно, что основная грппа закозов ноходится
# в районе 50 добавлений в корзину на сумму до 50т.р.
# Но при использовании калькулятора размеров есть аномальные выбросы
# как по кол-ву добавлений, так и по суммк добавлений,
# а при использовании таблицы размеров аномальные значения есть только по сумме


summary(test_group)
summary(control_group)

# Рассмотрим числовые данные предоставленой выборки
# Среднии значения по добавлению товара в корзину имеют не значительные 
# расхождения между обоими вариантами. 

# H0: P_old = P_new
# H1: P_old < P_new

boostr_cnt <- boostrap(control_cnt, test_cnt, 1000)
boostr_sum <- boostrap(control_sum, test_sum, 1000)

cnt_diff <- unlist(boostr_cnt[1])
sum_diff <- unlist(boostr_sum[1])

par(mfrow = c(1, 2))
hist(sum_diff, 
     col="skyblue", 
     border = "navy",
     main = "Распределение по сумме",
     xlab = "Суммы добавлений в корзину",
     xlim = c(-40000, 30000))
abline(v=quantile(sum_diff, 0.05), lwd=2, col="red")
abline(v=quantile(sum_diff, 0.95), lwd=2, col="red")

hist(cnt_diff, 
     col="skyblue", 
     border = "navy",
     main = "Распределение по кол-ву",
     xlab = "Кол-во добавлений в корзину")
abline(v=quantile(cnt_diff, 0.05), lwd=2, col="red")
abline(v=quantile(cnt_diff, 0.95), lwd=2, col="red")


# Вывод: p-value  < 0.05 - H1 отвергаем, разница нет. для
# Вывод: На основании проведенного иследования мы видим, 
# что нет разницы будем ли мы использовать таблицу размеров или 
# будем использовать калькулятор размеров

