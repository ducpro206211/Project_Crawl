import requests
import pandas as pd


dict_category = {
    "sach_da": "https://tiki.vn/lam-sach-da-mat/c11232?page={page}",
    "mat_na": "https://tiki.vn/mat-na-cac-loai/c1601?page={page}",
    "xit_khoang" : "https://tiki.vn/xit-khoang/c5872?page={page}",
    "da_mat" : "https://tiki.vn/cham-soc-vung-da-mat/c3424?page={page}",
    "trang_diem" : "https://tiki.vn/trang-diem/c11727?page={page}",
    "toner" : "https://tiki.vn/nuoc-hoa-hong-toner/c2347?page={page}",
    "chong_nang" : "https://tiki.vn/kem-chong-nang/c3422?page={page}",
    "tri_mun" : "https://tiki.vn/san-pham-tri-mun/c3426?page={page}",
    "kemsua_duong_da" : "https://tiki.vn/kem-va-sua-duong-da/c17170?page={page}",
    "sua_rua_mat" : "https://tiki.vn/sua-rua-mat/c1583?page={page}",
    "tay_te_bao_chet" : "https://tiki.vn/tay-te-bao-chet/c8206?page={page}",
    "tay_trang": "https://tiki.vn/tay-trang/c11605?page={page}",
    "chong_lao_hoa" : "https://tiki.vn/chong-lao-hoa-da/c5893?page={page}"
}
dict_API = {
    "sach_da"     : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=300&include=advertisement&aggregations=2&trackity_id=527749d7-0a68-f53e-54b5-fe2da48136f2&category=11232&page=1&sort=top_seller%3Fpage%3D5&urlKey=lam-sach-da-mat",
    "mat_na"      : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=1601&page=1&urlKey=mat-na-cac-loai",
 "Xit_khoang"     : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=5872&page=1&urlKey=xit-khoang",
     "da_mat"     : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=3424&page=1&urlKey=cham-soc-vung-da-mat",
 "trang_diem"     : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=11727&page=1&urlKey=trang-diem",
      "toner"     : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=2347&page=1&urlKey=nuoc-hoa-hong-toner",
"kem_chong_nang"  : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=3422&page=1&urlKey=kem-chong-nang",
    "tri_mun"     : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=3426&page=1&urlKey=san-pham-tri-mun",
"duong_da"        : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=17170&page=1&urlKey=kem-va-sua-duong-da",
"sua_rua_mat"     : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=1583&page=1&urlKey=sua-rua-mat",
"tay_te_bao_chet" : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=8206&page=1&urlKey=tay-te-bao-chet",
"tay_trang"       : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=11605&page=1&urlKey=tay-trang",
"chong_lao_hoa"   : "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=5893&page=1&urlKey=chong-lao-hoa-da"
}
def crawl_sach_da() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    sach_da_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=527749d7-0a68-f53e-54b5-fe2da48136f2&category=11232&page={page}&sort=top_seller%3Fpage%3D5&urlKey=lam-sach-da-mat"
    data_sachda = pd.DataFrame()
    for page_index in range(5):
        r = requests.get(sach_da_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_sachda = data_sachda.append(file)

    data_sachda = data_sachda.to_csv('E:\sachda.csv')
def crawl_matna() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    matna_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=1601&page={page}&urlKey=mat-na-cac-loai"
    data_matna = pd.DataFrame()
    for page_index in range(50):
        r = requests.get(matna_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_matna = data_matna.append(file)

    data_matna = data_matna .to_csv('E:\matna.csv')
def crawl_xitkhoang() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    xitkhoang_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=5872&page={page}&urlKey=xit-khoang"
    data_xitkhoang = pd.DataFrame()
    for page_index in range(10):
        r = requests.get(xitkhoang_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_xitkhoang = data_xitkhoang.append(file)

    data_xitkhoang = data_xitkhoang.to_csv('E:\\xitkhoang.csv')
def crawl_damat() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    damat_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=3424&page={page}&urlKey=cham-soc-vung-da-mat"
    data_damat = pd.DataFrame()
    for page_index in range(13):
        r = requests.get(damat_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_damat = data_damat.append(file)

    data_damat = data_damat.to_csv('E:\\damat.csv')
def crawl_trangdiem() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    trangdiem_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=11727&page={page}&urlKey=trang-diem"
    data_trangdiem = pd.DataFrame()
    for page_index in range(5):
        r = requests.get(trangdiem_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_trangdiem = data_trangdiem.append(file)

    data_trangdiem = data_trangdiem.to_csv('E:\\trangdiem.csv')
def crawl_toner() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    toner_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=2347&page={page}&urlKey=nuoc-hoa-hong-toner"
    data_toner = pd.DataFrame()
    for page_index in range(37):
        r = requests.get(toner_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_toner = data_toner.append(file)

    data_toner = data_toner.to_csv('E:\\toner.csv')
def crawl_chongnang() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    chongnang_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=3422&page={page}&urlKey=kem-chong-nang"
    data_chongnang = pd.DataFrame()
    for page_index in range(31):
        r = requests.get(chongnang_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_chongnang = data_chongnang.append(file)

    data_chongnang = data_chongnang.to_csv('E:\\chongnang.csv')
def crawl_trimun() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    trimun_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=3426&page={page}&urlKey=san-pham-tri-mun"
    data_trimun = pd.DataFrame()
    for page_index in range(38):
        r = requests.get(trimun_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_trimun = data_trimun.append(file)

    data_trimun = data_trimun.to_csv('E:\\trimun.csv')
def crawl_duongda() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    duongda_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=17170&page={page}&urlKey=kem-va-sua-duong-da"
    data_duongda = pd.DataFrame()
    for page_index in range(50):
        r = requests.get(duongda_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_duongda = data_duongda.append(file)

    data_duongda = data_duongda.to_csv('E:\\duongda.csv')
def crawl_suaruamat() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    suaruamat_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=1583&page={page}&urlKey=sua-rua-mat"
    data_suaruamat = pd.DataFrame()
    for page_index in range(50):
        r = requests.get(suaruamat_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_suaruamat = data_suaruamat.append(file)

    data_suaruamat = data_suaruamat.to_csv('E:\\suaruamat.csv')
def crawl_taytebaochet() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    taytebaochet_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=8206&page={page}&urlKey=tay-te-bao-chet"
    data_taytebaochet = pd.DataFrame()
    for page_index in range(16):
        r = requests.get(taytebaochet_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_taytebaochet = data_taytebaochet.append(file)

    data_taytebaochet = data_taytebaochet.to_csv('E:\\taytebaochet.csv')
def crawl_taytrang() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    taytrang_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=11605&page={page}&urlKey=tay-trang"
    data_taytrang = pd.DataFrame()
    for page_index in range(41):
        r = requests.get(taytrang_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_taytrang = data_taytrang.append(file)

    data_taytrang = data_taytrang.to_csv('E:\\taytrang.csv')
def crawl_chonglaohoa() :
    headers = {'accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
               }
    chonglaohoa_API_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=2049b810-664d-542f-a535-8e3866ec683a&category=5893&page={page}&urlKey=chong-lao-hoa-da"
    data_chonglaohoa = pd.DataFrame()
    for page_index in range(10):
        r = requests.get(chonglaohoa_API_url.format(page=page_index + 1), headers=headers)
        file = pd.json_normalize(r.json()['data'])
        data_chonglaohoa = data_chonglaohoa.append(file)

    data_chonglaohoa = data_chonglaohoa.to_csv('E:\\chonglaohoa.csv')




