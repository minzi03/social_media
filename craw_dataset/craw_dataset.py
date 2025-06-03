from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import pandas as pd
from bs4 import BeautifulSoup
# import time
from selenium.webdriver.common.action_chains import ActionChains
# 1. Khai báo browser
browser = webdriver.Chrome()

# 2. Mở thử một trang web
# browser.get("https://www.facebook.com/nhatkyphaothu.sc/posts/pfbid0aEgwndURov3NTkZAnkxvYFuv5codz6d2959CNYn8weqTvMWoo9Q4wH65Qv1p9XLWl")  
# browser.get("https://www.facebook.com/GAMeSportsVN/posts/pfbid02Dza6ezhT9zBSDDxiJjvxX33DSv3CoAW6iFBEhbs7mkuNE3MkD3YQjXb4LLt81Fppl")  
# browser.get("https://www.facebook.com/GAMeSportsVN/posts/pfbid02U3VpaYApVLSUax6b3Cy76LYxxSbfWwiq1jVDAcH3kDoTL6KT3CnZqAYZTaeiyhufl")  
# browser.get("https://www.facebook.com/GAMeSportsVN/posts/pfbid02shBBAp12yUG4ZDahunyUmpcsPNmdjmhkRCTBSJRiJBangcimL5S6m9cwhjkM1PwPl")  
# browser.get("https://www.facebook.com/500broslienminh/posts/pfbid02Vyf2igHMvcF8EKGGDep9UiGa8jY6XAfNV3SHA1B5qsJTN7sFp4EQddzXvFTonPFDl")  
# browser.get("https://www.facebook.com/LCKTiengViet/posts/pfbid02muFF6e5P9cRwnbsFvVzsB3e8tn8KNeUP5aULmLqEiSLfn1UmhDfRVDdd5JZB8K5jl")  
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid02VWgVAcs2cmf4G83MFqovYMNt8xCW6BzbL8K7RmBKztimtkNYXYEvWtXJe4Zen8UZl")  
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid024aQqFTGYP4KbUEZbdUS5jfHfVJkJLuGyZNd29gvt4GGGocFyYkAzD38b9Sq5Nmbwl")  
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid02JsCyMVxBnAf9jvDJpfsZ9wfpkotpZikCcXKNbzq7qc4zXfizfoYFV6tDpyt2ytaxl")  
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid02S1LEPFYfzfQknjv1k4G2T2vTfnWNhZPC1n4UWbqV97zfjW1T78dHXrizMVtA8vP8l?__cft__[0]=AZVHGJ5fyFghP76p-nSx9J7N-OEGdoIOrYfCVwSO4o7L4yYT0QzsdMsFO7nO69Niu5N1_hNI29Zskr9iO-LhOJbrcw-AQjOJGHkRK5PTO674sJAMmtZFHUo9cxpNMDy4ECE7SJgfYNQxf-lVMDg5QT4v0iIMgNA2wNSjXNt6nbaS-A&__tn__=%2CO%2CP-R-R")  
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid0Gm15TwJYN4u75HhVzfFeYs9sWkwMKGmKz3ptLQ2xsKJ9DkZhpD42uycv9ZcwfgaWl?__cft__[0]=AZVCEBn8R58u95vhF0NBmjfr3Dy424Krp_fkOMTyYgbn7xhz5oVMT1Up-vewB3akASqAzTu_ZF4mwc-2zDPcAXgDAv6K5NtxtPCjmd8SPr64ZnQmAVKfgLw7h_qR18lCAa4iOOSk14uT1d59awtoQ3WjXO57RF9266jvj9aT-O9Q3Q&__tn__=%2CO%2CP-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid022Bw5rUGKD1xGNHhvwQejaeaAX9dYk9BuKfEhcHKA8eZKc38Cme7jdVNa8M5GJG29l?__cft__[0]=AZUtE4pGS011T4zyV6zCfA9mTMz-6ZuJURF3x1nuoTooYJPWKEBJls6nIUu0P791uzg1Lh0DYMwUu7ebo3YscABVOnWJqFd_prgZPK_KY1evmaewN956XP8jVhm9hzu9eUo0b5QW5hXTm79EF5EMv-EZznEczkk84UZxzIH5Cia_EPOe15F8KRb1sA4vLnqNyW1mBMNwbCDtcslCH1yp4hKQ&__tn__=%2CO%2CP-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid02j2hatLTyYYxemifVfqTcfeeD59H9idNCsdSmzqhyrAZ5G3XSmfCvi39Bwvg8V4cpl?__cft__[0]=AZUPyuK1fBUP5Ht__cjRCfOqQoU-iyheai4gFAPVfbB56WHQa2jertVmj5nGAM3mQDp5zzeoVY3EpTdj4w6BpZhcJGfmFwl94OGgTmWhimvBSX7TEccHuKFX_GWKE2jo1UDtNlFEC2TN-89WvjjKEIX1Z_giFf2PjCRE5OQxzm8tVw&__tn__=%2CO%2CP-R-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid02bGRjajhBsit2kist81dLXmwz7vNWaZkWdYcsawY7SLyhDpt12fyKB2cGuiGCLjxql?__cft__[0]=AZXK0RoiW7f1QIDnE7eGfHbz2VnCtdqBBw8AWEfVLU8hrHeW75aYCsap45YZYyaO0yg8t5lXA50r5RTKlFI3DokFgG-jaFIpsuJsYi-86joDPjBeB792tnQD5Og75qufBoz3j77IyNhKQRZBpzTvrYhKyMROml4mMqUI9gqFNgO4bg&__tn__=%2CO%2CP-R-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid031MDyerkfj2ggVPJtHDRDSZQEcw9W4yYJCDB1JyuKrfjEsUWVLMANDJRTVmkx48NYl?__cft__[0]=AZURdNEdnl_UOVheZVvhh5rVIFvObC55a8Xjs0ColyNlXY1xaci4bmRSmOfonrfLZ58-S8wolEY8wb1IQ49VAR7b2cBWdahA_WCbn6qTUaSu7T8FsZVbJA6aHlLBQGsxstyhcLE9tK2HgYCn5af4JoOBRwrUHRlYT47avodDT2KiSA&__tn__=%2CO%2CP-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid08gbkchFAaugrd75xtC7CYQ8KQCuTPsZ5q6U4EwGhK4xZMktgETxkWTePeRrqNTjJl?__cft__[0]=AZXsMHBRIKgW_wgt5oAVzj_AQPNXOkwG09xaE2yqsvYfav8vAgMq9ZTXR6WNX0fBLKKCY733Z8ys_f7Ipu2Va4xEBHR8hn8fQuOR8-yEDib8hIRWXjeXwXlxetWVc_Q7DvlxCqH1vMO0wfaGBe3jecjgR-PjIwKhrzSU4_NFuMmSog&__tn__=%2CO%2CP-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid02BaM2a1FvyHGLATHfG5bWGjepTu9uYd6LefuJA6ETp3KoREMhU6QuE2avLutvtYnnl?__cft__[0]=AZVpFzWUpcDJADJWjKgZnLiD0pPJXr2FIc2eqZkDH4P8pgBn1g0WrHa_ua7Ma6AJXAyknL_fcgM2-eUsbV9Vbl0uDiKTumhT44Tq9FKYHnTfauqvb6QH4cw04e8HT6OP2DpoBw77POb6CvIhZI6n2gj-Tw4lEgfYtqnJ7EvQhqCbUQ&__tn__=%2CO%2CP-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid027MH7ZDdfi9WKFJUpUyiVkhSAR7g1jam4nS8CM8GkQLYRYncDgS9ACh9VR3ZDKrLhl?__cft__[0]=AZWbzWAEAiWduwTwPPkO_fv-iUsQzrbLyFp4SheBc2IXQgCK8xYbH1g8RA4Zut_dLdDApRfUjG5SVcpNadQdPVoFHwcIeG0_S1ikpIMbud54HkwBvuzoR77VhoLD1P9dv4aOgBavz6GLMeaotNS0HohT1V_wO3hOH0AODf3s1FIc_A&__tn__=%2CO%2CP-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid02fjum8GwhgeYiZTvFQLgfkW2vwELkiXEWFQyBKsqcrCNXxTH3TcbshTmWbxKJUFzWl?__cft__[0]=AZXY3eOqTOuQx1NcyU69bsZ2KCvloQR623oF1421Pg2VDY33Yx7eaWFWhIxFQ7ADAS99Qr_svbCRAqXEGG9o5jHtLP36yYsVG9iY0Vya0HRd63dbI3DH9xyZa2bhLQ5RG0xCDvGkFjbUperhdarQRou6uYSSQFlrYHXKTYJJ7Ek6rw&__tn__=%2CO%2CP-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid0947b2cvmUShRfxuz7Tk2PUWAC61YuLLa4ivs2r5raRPtVZt1WdM23EXJpNnk7Q6nl?__cft__[0]=AZVXYBNxtpHtj_SSfsns279kGfDTcKiFX-SAXVIlAA21yI9SEglGkeWlspHHTn_FGxl5fy2coyziXeYzLN59YxzU4yuA153fEKDF4WlJgV4uFOk6ZSDiLFeI2ADUqlw-1-jzJvuj2sWLNSAlKWTISj7VwVe1vMTL_0WX3uyYVa12pDT3q0C6bgj4isdVxyoKuYJ1Fim63g5MhS1RQCPyxnoP&__tn__=%2CO%2CP-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid02KdSKPacumTf7tqP845SsLtZAhgzfpfoUpiUeVWWburXym5fMoucrKFMi4Ea831qWl")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid02fjum8GwhgeYiZTvFQLgfkW2vwELkiXEWFQyBKsqcrCNXxTH3TcbshTmWbxKJUFzWl")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid0X5evWfTTP6j283UmBCCQfmMwmmt1oQ1djKHr2d2NBBLc8yR2Yjq1nX376QwaBELzl?__cft__[0]=AZXcU_0qdcExe79ZuzvQd3RuQZg56zf_-WYjp5xarNYumEusmcJ-GuUAFgTQTGE9PMXZVewNHeaRBvX6Uz0YxcANTZ9MMX8ztqkcmQPvanWG6em5ToXnfm2Mv9MCuWofAvnBLtsLs6i4fOKr8fjgksboz4W5JZhYtaq6JyDGIUIOzA&__tn__=%2CO%2CP-R-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid0y4s1ASuyyQerDASeVD9bHZV4oDTdTz7Sw6Rrb1Bi4G6A656sXcciLfotrLzFCNBkl")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid02qDtkN9Rpnuy6Er63dCrJYf9cmiFgbrsyqXB6PZySo3Pzk7C7hxvKS8my23jrDzbil")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid0323Qyxg8qChLDgXHGtPLsa2auR5ffAkc6crbj38tSLrYM731EcKGDzRRSsU9V9Hckl?__cft__[0]=AZXMEjwJqnJJ7K8fvG637SQiDv0ewaB3mHav-9serz-nHSNR4Q2Hl3xVA7b56kjE1dzA_130OS4cAqYwLV7AUHGB39SAbRFJuwcgHqS6a9O6bO-MdTrbnp8sZ3P4bCD8oVtklhPON34ej3lv3vUuPjN0-hbPDpOzx6QEYj9glgSpbQ&__tn__=%2CO%2CP-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid0HZrU87ixURuzC6tzwgWEqqiiKBtN6eQ7t3c6uoKv1pjmR5ZBbVUrKuhLh4YZEfP7l")
# browser.get("https://www.facebook.com/theanh28express/posts/pfbid0efE3jduRuhZAZoKY5YMyNK35rXHQJj8YroSGsSN2rFF3qaXZpzCXSp6dG4jHTthSl?__cft__[0]=AZUFshQWIE_IK3dZKnOl7B7PZhoCcoNW4zs_Mmg-ximVgXJBhTnTqup2XBkHHWfaM8DsnwsMsWbGp8gMq1oGie6lWw-4GzIJz5jcz2sGehO5D1HJXvCZu9gDOb2G_TRqIsbEiPLMmgnRcRCbT4bryS_GPGb5lF1Hr53BcrQhI7cYRQ&__tn__=%2CO%2CP-R")
# browser.get("https://www.facebook.com/theanh28express/posts/pfbid02Kop7dJbheA3EikqFPMycMPx7ygXLaeP63GTthePUka1qtsYc6Q2moLTgSWnXyp1Bl?__cft__[0]=AZXx5NIY1f7ZBzIbHS-cu-1zZZWLCxGRDDQL37s_4tA9OEET3HZdPwQX3avSdvksBxN5EXPVy6eqlyNezIrMtuaoob0O1WQG0VsYrWs4Jxhb5QBXCQACYoZ7PA3jtMnIuuvxqmJSdLoiBPOYDe7SZAPQArg-BWimJaTc--oeiffrUA&__tn__=%2CO%2CP-R-R")
# browser.get("https://www.facebook.com/theanh28express/posts/pfbid032X9sC9qb1awZuert7JU7ki7ZHWChTaf3boUSk5WU3FF1bznoJdtgNBiU6YyJSci5l?__cft__[0]=AZWkLYdBinHM0WOutlaOoNoEqyOR-P-J5mhQ_JkNDPt_qRAUbjZoHKgWmGX7u574lAc-gfUdQoSTL_aOzOMnoHdKx3QHvgc7anTG84dKXL_cosszrONFqIA5MV01FQFZzxZAJuNEBmhuJFRFnvhhvUOLkLhYGK0V20As7cHQp1Yj2g&__tn__=%2CO%2CP-R-R")
# browser.get("https://www.facebook.com/theanh28express/posts/pfbid028PTGv88b5bWdRJEGMjwcC7c5CFmjnreeDV551J72qmfBSGYENxvT7n9wKDP2dFyVl?__cft__[0]=AZXC0wYggvPJKpOM69THqr9S9Mhv7aWfZWQdi3vQpk_A4LXBs4QXK2SZI_Npvox5hFdZr0yH1JIsKUtDaezOMjGJk5MxfKZVaf9vCg9oyCrebIX1bANb--dRjZ6AQrK9vmm0dcGi-NU84WojGPwe9T4tJvlU8XpFfnMbdMSZYaCg-Q&__tn__=%2CO%2CP-R-R")
# browser.get("https://www.facebook.com/bmsb.vnn/posts/pfbid0HtkJnQw4vSywarYjzz7g1LTTpWdK5WHPBNJMYTSnq6MgUCkuiKLnFm3o7BQSzgCtl?__cft__[0]=AZWJtXraqZ1UMcwid1rp7Nxg5qvnqgQcgsWn5HZXJG1VWYKdzrvQSiEJE2tVuZfv6yyoSzb5yWoI2--qtrYEQjSpn1SdZb1fCQpPd1DHvXlRh2oJ8b4Z_-qLPHvj27PNzwjd6OUG8XjtrGm14VKC32raUZGnV15s35gd0Q0ZcWn11Q&__tn__=%2CO%2CP-R-R")
browser.get("")
# browser.get("")
# browser.get("")
# browser.get("")
# browser.get("")
# browser.get("")
# browser.get("")
# browser.get("")
# browser.get("")
# browser.get("")

# 2a. Điền thông tin vào ô user và pass
# txtUser = browser.find_element(By.ID, "email")
# txtUser.send_keys("hoanhnguyen820@gmail.com") # <---  Điền username thật của các bạn vào đây
# txtPass = browser.find_element(By.ID,"pass")
# txtPass.send_keys("hoanh12345")
# # 2b. Submit form
# txtPass.send_keys(Keys.ENTER)


sleep(5)
# 3. đổi chế độ lọc bình luận
link1 = browser.find_element(By.XPATH,"//div[@aria-haspopup='menu']")             
link1.click()
sleep(5)
# 3b. Lọc tất cả bình luận
# Tìm <span> theo nội dung
span = browser.find_element(By.XPATH, "//span[contains(text(), 'All comments')]")
span.click()

actions = ActionChains(browser)
prev_count = 0
same_count = 0
# Cuộn từ từ bằng PAGE_DOWN
for _ in range(500):  # Cuộn tối đa 500 lần, tránh lặp vô hạn
    actions.send_keys(Keys.PAGE_DOWN).perform()  # Cuộn trang xuống
    # sleep(2)  # Chờ Facebook load thêm comment mới
    sleep(random.uniform(2,4))
    comment_list = browser.find_elements(By.XPATH, "//div[@dir='auto'][@style='text-align: start;']")
    current_count = len(comment_list)  # Đếm số comment hiện tại

    if current_count == prev_count:  # Nếu không có comment mới
        same_count += 1
    else:
        same_count = 0  # Reset nếu có thêm comment mới

    prev_count = current_count

    if same_count >= 3:  # Nếu 3 lần liên tiếp không có comment mới
        break  # Dừng lại vì có thể đã load hết


# # 5. Tìm tất cả các comment và ghi ra màn hình (hoặc file)
# comment_list = browser.find_elements(By.XPATH, "//div[contains(@aria-label, 'Comment by')]")

sleep(5)
# input("Bạn đã scroll xong, nhấn Enter để tiếp tục...")

# Lặp trong tất cả các comment và hiển thị nội dung comment ra màn hình
sleep(5)
# for comment in comment_list:
#     print("*", comment.text)

# 5. Lặp trong tất cả các comments và lưu comment
record = []
for comment in comment_list:
    html = comment.get_attribute('innerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    # Xóa tất cả thẻ <a> bên trong comment
    for a in soup.find_all('a'):
        a.decompose()
    # Lấy nội dung còn lại
    clean_text = soup.get_text(strip=True)
    record.append(('', comment.text))  # Label để trống
# Tạo DataFrame
df = pd.DataFrame(data=record, columns=['Label', 'Comment'])
# Hiển thị thử 5 dòng đầu
print(df.head())
# Lưu vào file CSV (append mode)
df.to_csv('Dataset.csv', mode='a', encoding="utf-8-sig", index=False)

# 3. Dừng chương trình 5 giây
sleep(5)

# 4. Đóng trình duyệt
browser.close()