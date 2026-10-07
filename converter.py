# Python backend fallback tool for Plist processing
import plistlib

def adjust_ipa_metadata(plist_path):
    with open(plist_path, 'rb') as fp:
        pl = plistlib.load(fp)
    
    pl['CFBundleShortVersionString'] = '1.4'
    pl['CFBundleVersion'] = '1.4'
    pl['MinimumOSVersion'] = '2.0'
    
    with open(plist_path, 'wb') as fp:
        plistlib.dump(pl, fp)
