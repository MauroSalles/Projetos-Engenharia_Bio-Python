# --- DICIONÁRIO DE TRADUÇÃO (CÓDONS -> AMINOÁCIDOS) ---
# Este dicionário mapeia o código genético do RNA para proteínas.
TABELA_GENETICA = {
    'UUU': 'Fenilalanina', 'UUC': 'Fenilalanina', 'UUA': 'Leucina', 'UUG': 'Leucina',
    'CUU': 'Leucina', 'CUC': 'Leucina', 'CUA': 'Leucina', 'CUG': 'Leucina',
    'AUU': 'Isoleucina', 'AUC': 'Isoleucina', 'AUA': 'Isoleucina', 'AUG': 'Metionina (Início)',
    'GUU': 'Valina', 'GUC': 'Valina', 'GUA': 'Valina', 'GUG': 'Valina',
    'UCU': 'Serina', 'UCC': 'Serina', 'UCA': 'Serina', 'UCG': 'Serina',
    'CCU': 'Prolina', 'CCC': 'Prolina', 'CCA': 'Prolina', 'CCG': 'Prolina',
    'ACU': 'Treonina', 'ACC': 'Treonina', 'ACA': 'Treonina', 'ACG': 'Treonina',
    'GCU': 'Alanina', 'GCC': 'Alanina', 'GCA': 'Alanina', 'GCG': 'Alanina',
    'UAU': 'Tirosina', 'UAC': 'Tirosina', 'UAA': 'PARADA', 'UAG': 'PARADA',
    'CAU': 'Histidina', 'CAC': 'Histidina', 'CAA': 'Glutamina', 'CAG': 'Glutamina',
    'AAU': 'Asparagina', 'AAC': 'Asparagina', 'AAA': 'Lisina', 'AAG': 'Lisina',
    'GAU': 'Aspartato', 'GAC': 'Aspartato', 'GAA': 'Glutamato', 'GAG': 'Glutamato',
    'UGU': 'Cisteína', 'UGC': 'Cisteína', 'UGA': 'PARADA', 'UGG': 'Triptofano',
    'CGU': 'Arginina', 'CGC': 'Arginina', 'CGA': 'Arginina', 'CGG': 'Arginina',
    'AGU': 'Serina', 'AGC': 'Serina', 'AGA': 'Arginina', 'AGG': 'Arginina',
    'GGU': 'Glicina', 'GGC': 'Glicina', 'GGA': 'Glicina', 'GGG': 'Glicina'
}

def traduzir_sequencia(dna):
    # Converte tudo para maiúsculo para evitar erros
    dna = dna.upper().strip()
    
    # PASSO 1: Transcrição (Troca Timina por Uracila)
    rna = dna.replace('T', 'U')
    
    # PASSO 2: Tradução (Lê de 3 em 3 letras)
    proteina = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if len(codon) == 3:
            aminoacido = TABELA_GENETICA.get(codon, "Desconhecido")
            if aminoacido == "PARADA":
                break
            proteina.append(aminoacido)
            
    return rna, proteina

# --- INTERFACE DE TERMINAL ---
print("="*40)
print("     SISTEMA DE ANÁLISE GENÉTICA v1.0")
print("="*40)

dna_input = input("Digite a sequência de DNA (ex: ATGCGT...): ")
rna, proteina_final = traduzir_sequencia(dna_input)

print("-" * 40)
print(f"[>] RNA Mensageiro: {rna}")
print(f"[>] Cadeia de Proteínas: {' -> '.join(proteina_final)}")
print("-" * 40)