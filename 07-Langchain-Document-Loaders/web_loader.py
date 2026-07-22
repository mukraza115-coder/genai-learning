from langchain_community.document_loaders import WebBaseLoader




url="https://www.daraz.pk/products/macbook-air-13-in-m5-i1958244187-s14019002525.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Amacbook%253Bnid%253A1958244187%253Bsrc%253ALazadaMainSrp%253Brn%253A2b325f865d98e2e8d39e1ebd6b7c87b4%253Bregion%253Apk%253Bsku%253A1958244187_PK%253Bprice%253A388999%253Bclient%253Adesktop%253Bsupplier_id%253A6005657392001%253Bsession_id%253A%253Bbiz_source%253Ahttps%253A%252F%252Fwww.daraz.pk%252F%253Bslot%253A1%253Butlog_bucket_id%253A470687%253Basc_category_id%253A7902%253Bitem_id%253A1958244187%253Bsku_id%253A14019002525%253Bshop_id%253A2559934%253BtemplateInfo%253A&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Punjab&price=388999&priceCompare=skuId%3A14019002525%3Bsource%3Alazada-search-voucher%3Bsn%3A2b325f865d98e2e8d39e1ebd6b7c87b4%3BoriginPrice%3A38899900%3BdisplayPrice%3A38899900%3BisGray%3Afalse%3BsinglePromotionId%3A50000079923005%3BsingleToolCode%3AflashSale%3BvoucherPricePlugin%3A0%3Btimestamp%3A1784704661223&ratingscore=&request_id=2b325f865d98e2e8d39e1ebd6b7c87b4&review=&sale=0&search=1&source=search&spm=a2a0e.searchlist.list.1&stock=1"
loader=WebBaseLoader(url)

docs=loader.load()

print(docs)