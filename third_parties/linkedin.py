##marco_response: https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json
import os
import requests


# gist_response = requests.get("https://gist.githubusercontent.com/jlozanop42/945f4e760631a74617dfe6e0ae715d3d/raw/cc7f99081ae69f93aadd2fe6f167ba5424daa463/sebastian-lozano.json")
# print(gist_response.json())
# print(gist_response.json()['full_name'])
def scrape_linkedin_profile():
    response = requests.get(
        "https://gist.githubusercontent.com/jlozanop42/945f4e760631a74617dfe6e0ae715d3d/raw/c40537711d2cd502421ee8a936b16c6a5b910efc/sebastian-lozano.json")
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


# To use the proxycurl linkedin feature
def scrape_linkedin_profile_with_curl_proxy(linkedin_profile_url: str):
     print(linkedin_profile_url)
     api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
     header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

     response = requests.get(
         api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic)

     data = response.json()
     data = {
         k: v
         for k, v in data.items()
         if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
     }
     if data.get("groups"):
         for group_dict in data.get("groups"):
             group_dict.pop("profile_pic_url")

     return data
