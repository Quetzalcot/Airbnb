
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.common.exceptions import  NoSuchElementException
import  pandas as pd

driver = webdriver.Chrome(executable_path=".venv/chromedriver.exe")
driver.get('https://www.airbnb.com.vn/s/Ho-Chi-Minh-City--Vietnam/homes')
driver.implicitly_wait(5)

print("Now Loading....")
list,link = [],[]
count = 0
def get_district(address):
    comma_locate = address.find(',')
    if comma_locate != -1:
        return  address[:comma_locate]
    return  address

while True:
    driver.implicitly_wait(5)
    try:
        listroom =driver.find_elements(By.CSS_SELECTOR, 'div.c1l1h97y.atm_d2_1kqhmmj.dir.dir-ltr ')
        for room in listroom:
            try:
                link.append(room.find_element(By.CSS_SELECTOR, ' div > div > div > div > a').get_attribute('href'))
            except NoSuchElementException:
                continue

        next = driver.find_element(By.CSS_SELECTOR, '#site-content > div > div.pbmlr01.atm_h3_t9kd1m.atm_gq_n9wab5.dir.dir-ltr > div > div > div > nav > div > a.l1ovpqvx.atm_1he2i46_1k8pnbi_10saat9.atm_yxpdqi_1pv6nv4_10saat9.atm_1a0hdzc_w1h1e8_10saat9.atm_2bu6ew_929bqk_10saat9.atm_12oyo1u_73u7pn_10saat9.atm_fiaz40_1etamxe_10saat9.c1ytbx3a.atm_mk_h2mmj6.atm_9s_1txwivl.atm_h_1h6ojuz.atm_fc_1h6ojuz.atm_bb_idpfg4.atm_26_1j28jx2.atm_3f_glywfm.atm_7l_hkljqm.atm_gi_idpfg4.atm_l8_idpfg4.atm_uc_10d7vwn.atm_kd_glywfm.atm_gz_8tjzot.atm_uc_glywfm__1rrf6b5.atm_26_zbnr2t_1rqz0hn_uv4tnr.atm_tr_kv3y6q_csw3t1.atm_26_zbnr2t_1ul2smo.atm_3f_glywfm_jo46a5.atm_l8_idpfg4_jo46a5.atm_gi_idpfg4_jo46a5.atm_3f_glywfm_1icshfk.atm_kd_glywfm_19774hq.atm_70_glywfm_1w3cfyq.atm_uc_aaiy6o_9xuho3.atm_70_18bflhl_9xuho3.atm_26_zbnr2t_9xuho3.atm_uc_glywfm_9xuho3_1rrf6b5.atm_70_glywfm_pfnrn2_1oszvuo.atm_uc_aaiy6o_1buez3b_1oszvuo.atm_70_18bflhl_1buez3b_1oszvuo.atm_26_zbnr2t_1buez3b_1oszvuo.atm_uc_glywfm_1buez3b_1o31aam.atm_7l_1wxwdr3_1o5j5ji.atm_9j_13gfvf7_1o5j5ji.atm_26_1j28jx2_154oz7f.atm_92_1yyfdc7_vmtskl.atm_9s_1ulexfb_vmtskl.atm_mk_stnw88_vmtskl.atm_tk_1ssbidh_vmtskl.atm_fq_1ssbidh_vmtskl.atm_tr_pryxvc_vmtskl.atm_vy_1vi7ecw_vmtskl.atm_e2_1vi7ecw_vmtskl.atm_5j_1ssbidh_vmtskl.atm_mk_h2mmj6_1ko0jae.dir.dir-ltr')
        next.click()

    except NoSuchElementException:
        break
df1 = pd.DataFrame(link)
df1.to_csv("linkroom.csv")


print("50%")

df2 = pd.read_csv("linkroom.csv")
link = df2.iloc[:,1].to_numpy().flatten()

for room in link:

    driver.implicitly_wait(2)
    try:
        driver.get(room)
        try:
            close_butt = driver.find_element(By.XPATH, '/html/body/div[9]/div/div/section/div/div/div[2]/div/div[1]/button')
            close_butt.click()
        except NoSuchElementException:
            close_butt = 0

        try:
            name = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[1]/div[1]/div/div/div/div/div/section/div/div[1]/span[2]/h1').text
        except NoSuchElementException:
            try:
                name = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[1]/div[1]/div/div/div/div/div/section/div/div[1]/span/h1').text
            except NoSuchElementException:
                name = "NA"

        try:
            price = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/span/div/span[1]').text
        except NoSuchElementException:
            price = "NA"

        try:
            lo = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[5]/div/div/div/div[2]/section/div[2]').text
            locate = get_district(lo)
            if locate:
                1
            else:
                lo = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[5]/div/div/div/div[2]/section/div[4]/div/div/div/div[1]/h3').text
                locate = get_district(lo)
                if locate == "" or locate == " ":
                    locate = "NA"
        except NoSuchElementException:
            locate = "NA"

        try:
            rate = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[3]/div[2]').text
            if rate == "Mới":
                rate = "NA"
        except NoSuchElementException:
            try:
                rate = driver.find_element(By.CSS_SELECTOR,'#site-content > div > div:nth-child(1) > div:nth-child(3) > div > div._16e70jgn > div > div:nth-child(2) > div > div > div > a > div > div.a8jhwcl.atm_c8_vvn7el.atm_g3_k2d186.atm_fr_1vi102y.atm_9s_1txwivl.atm_ar_1bp4okc.atm_h_1h6ojuz.atm_cx_t94yts.atm_le_14y27yu.atm_c8_sz6sci__14195v1.atm_g3_17zsb9a__14195v1.atm_fr_kzfbxz__14195v1.atm_cx_1l7b3ar__14195v1.atm_le_1l7b3ar__14195v1.dir.dir-ltr > div:nth-child(2)').text
            except NoSuchElementException:
                rate = "NA"


        try:
            guest = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[1]').text
            livingroom = guest[0:1]
        except NoSuchElementException:
            livingroom = "0"

        try:
            bedrooms = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[2]').text
            bedroom = bedrooms[3:4]
            if bedroom == "P":
                bedroom = "1"
            if bedroom == "K":
                bedroom = "0"
        except NoSuchElementException:
            bedroom = "0"

        try:
            beds = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[3]').text
            bed = beds[3:4]
        except NoSuchElementException:
            bed = "0"

        try:
            bathrooms = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[4]').text
            bathroom = bathrooms[3:4]
            if bathroom == "K":
                bathroom = "0"
        except NoSuchElementException:
            bathroom = "0"

        list.append([name,price,locate, rate, livingroom, bedroom,bed,bathroom, room])
    except NoSuchElementException:
        break
df3 = pd.DataFrame(list)
df3.columns = ["Name", "Price", "Location", "Rate", "Living Room", "Bed Room", "Bed", "Bath Room", "Link"]
df3.index.name = "No"
df3.to_csv("listroom.csv")


print("100%")


driver.quit()