import cv2 as cv
import pytesseract


def main():
    # NOTE: 画像の読み込みとグレースケール化
    img = cv.imread('img/school-test.jpg')
    gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    """
    NOTE: OCR処理
    閾値を68 <= n < 70くらいだと必要な文字は取得できる。
    """
    ret, thresh_img = cv.threshold(gray_img, 68, 255, cv.THRESH_BINARY)
    cv.imwrite('img/thresh-img.jpg', thresh_img)
    text = pytesseract.image_to_string(thresh_img, lang='jpn')

    # NOTE: 空白行と改行を取り除く
    text = str(text).replace(' ', '').replace('\n', '')
    print(text)

    # NOTE:「学校」「大会」が含まれていたらにする。「最強」は取得できないため。
    if '学校' in text or '大会' in text:
        print('Yes')


if __name__ == '__main__':
    main()
