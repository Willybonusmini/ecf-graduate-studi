# -*- coding: utf-8 -*-
"""
Module: Automatisation de la Veille Technologique
Objectif: Extraction des flux de sécurité (CERT-FR) et DevOps
Auteur: Wilson Antonio Martins
"""
import urllib.request
import xml.etree.ElementTree as ET

def fetch_tech_watch(url: str, source_name: str) -> None:
    """Récupère et parse le flux RSS de la source spécifiée."""
    try:
        print(f"\n--- Audit de Veille : {source_name} ---")
        # Injection du header User-Agent pour prévenir le rejet HTTP 403
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            # Extraction stricte des 5 dernières alertes
            for item in root.findall('./channel/item')[:5]:
                title = item.find('title').text
                pub_date = item.find('pubDate').text if item.find('pubDate') is not None else "Date inconnue"
                print(f"[*] {pub_date} | {title}")
    except Exception as e:
        print(f"[!] Erreur de synchronisation avec {source_name}: {e}")

if __name__ == "__main__":
    # Point d'accès officiel du CERT-FR pour les alertes de cybersécurité
    cert_fr_rss = "https://www.cert.ssi.gouv.fr/alerte/feed/"
    fetch_tech_watch(cert_fr_rss, "CERT-FR (Alertes de Sécurité)")