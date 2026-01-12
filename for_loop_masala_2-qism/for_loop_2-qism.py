# #1-masala
# for son in range(1, 11):
#     print(son, end=" ")
# print("\n")
# # 2-masala
# for harf in "Python":
#     print(" -", harf)
# print()
# #3-masala
# ismlar = ["Ali", "Vali", "Dilnoza", "Madina", "Sobir"]
# raqam = 1
# for ism in ismlar:
#     print(f"{raqam}. {ism}")
#     raqam += 1
# #4-masala
# for son in range(2, 21, 2):
#     print(son, end=" ")
# #5-masala
# yigindi = 0
# for son in range(1, 51):
#     yigindi += son
# print("1 dan 50 gacha yig'indi:", yigindi)
# #6-masala
# sana = 0
# for son in range(1, 101):
#     if son % 3 == 0:
#         print(son, end=" ")
#         sana += 1
# print("\nJami:", sana, "ta son topildi!")
# #7-masala
# matn = "Python dasturlash juda qiziqarli va foydali"
# unlilar = "aeiouAEIOU"
# sanash = 0
# for belgi in matn:
#     if belgi in unlilar:
#         sanash += 1
# print("Matn:", matn)
# print("Unli harflar soni:", sanash)
# #8-masala
# sonlar = [45, 12, 89, 34, 67, 23, 91, 56, 78]
# eng_katta = sonlar[0]
# for son in sonlar:
#     if son > eng_katta:
#         eng_katta = son
# print("Eng katta son:", eng_katta)
# #9-masala
# sonlar2 = [34, 12, 89, 5, 67, 23, 91, 45]
# yigindi2 = 0
# max_son = sonlar2[0]
# min_son = sonlar2[0]
# sonlar1 = 0
# for son in sonlar2:
#     yigindi2 += son
#     sonlar1 += 1
#     if son > max_son:
#         max_son = son
#     if son < min_son:
#         min_son = son
# x = yigindi2 / sonlar1
# print("Sonlar:", sonlar2)
# print("Yig'indi:", yigindi2)
# print("Maksimum:", max_son)
# print("Minimum:", min_son)
# print("O'rtacha:", x)
# #10-masala
# matn2 = "Python"
# reverse = ""
# for harf in matn2:
#     reverse = harf + reverse
# print("Asl matn:", matn2)
# print("Teskari:", reverse)
# #11-masala
# print("=" * 70)
# print("           TO'LIQ KO'PAYTIRISH JADVALI (1-10)")
# print("=" * 70)
# for i in range(1, 11):
#     print()
#     print(f"{i} ning ko'paytma jadvali:")
#     print("-" * 30)
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)
# #12-masala
# print('      *\n     ***\n    *****\n   *******\n  *********\n ***********\n*************')
