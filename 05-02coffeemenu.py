menu = ['COFFEE','BEVERAGE','ADE']
coffee = ['에스프레소','아메리카노','카페라테','카페모카']

print('=' * 45)
#앞에 카테고리변수에 첫루프때 커피, 비버리지, 에이드 들어옴.
#리스트 for in 
for category in menu:
    print('{:^15s}'.format(category), end = ' ')
print()
print('=' * 45)

for ckind in coffee:
    print('{:^10s}'.format(ckind))
# :s 문자열형태. ^15 15는 15의 길이 오른쪽정렬. ^ 중앙 정렬.
    
