/* Site settings. Fill these in to switch features on; empty values leave them off.

   web3formsKey  Access key from web3forms.com (it's designed to be public).
                 Submissions are emailed to the address you registered there.
   gaId          Google tag / GA4 measurement ID, e.g. "G-XXXXXXXXXX".
                 Loads only after a visitor accepts the cookie banner.
   cfBeacon      Cloudflare Web Analytics token (Cloudflare dashboard > Web Analytics).
                 Cookieless, so it loads without the banner. Leave empty if the site
                 is proxied through Cloudflare with automatic Web Analytics turned on. */
window.SITE_CONFIG = {
  web3formsKey: "cbe536ca-6b46-40cb-b5d6-71ec02ef63d2",
  gaId: "",
  cfBeacon: "",
};
