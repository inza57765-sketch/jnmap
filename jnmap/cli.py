#!/usr/bin/env python3
"""
jnmap - Mini Scanner de Ports
Utilisation: jnmap <host> <ports>
Exemple: jnmap 192.168.1.1 80,443,8080
"""

import sys
import argparse
from jnmap.scanner import Scanner

def main():
    """Point d'entrée principal de la CLI"""
    
    parser = argparse.ArgumentParser(
        description='jnmap - Scanner de ports léger et rapide',
        epilog='Exemple: jnmap 192.168.1.1 80,443,8080-8090'
    )
    
    parser.add_argument('host', help='Adresse IP ou hostname à scanner')
    parser.add_argument('ports', help='Ports à scanner (ex: 80,443,8080-8090)')
    parser.add_argument('-t', '--timeout', type=int, default=1, 
                        help='Timeout par port en secondes (défaut: 1)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Mode verbeux')
    parser.add_argument('--version', action='version', version='jnmap 0.1.0')
    
    args = parser.parse_args()
    
    try:
        scanner = Scanner(args.host, timeout=args.timeout, verbose=args.verbose)
        results = scanner.scan(args.ports)
        
        print(f"\n{'='*50}")
        print(f"Scanner Results for {args.host}")
        print(f"{'='*50}\n")
        
        if results['open_ports']:
            print(f"✓ Ports OUVERTS: {results['open_ports']}")
        else:
            print("✗ Aucun port ouvert détecté")
        
        print(f"\nPorts scanés: {results['total_scanned']}")
        print(f"Temps d'exécution: {results['time']:.2f}s\n")
        
    except KeyboardInterrupt:
        print("\n\n[!] Scan annulé par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"[Erreur] {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
