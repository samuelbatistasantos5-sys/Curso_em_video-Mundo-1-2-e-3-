times = ('Palmeiras','Flamengo','Fluminense','Bahia','Botafogo','Corinthians','Cruzeiro','Red Bull Bragantino','Atlético-MG','São Paulo','Internacional','Athletico-PR','Santos','Mirassol','Grêmio','Coritiba','Vitória','Vasco','Remo','Chapecoense'
)

print("-="*45)
print(f"os 20 times da tabela são: {[times]}")
print("-="*45)
print(f"Os 5 primeiros times são: {times[:5]}")
print("-="*45)
print(f"Os 4 últimos são: {times[16:20]}")
print("-="*45)
print(f"Os times em ordem afalbética é: {sorted(times)}")
print("-="*45)
print(f"O time do Chapecoense está na {times.index('Chapecoense')+1}° posição")
print("-="*45)