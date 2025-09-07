from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Product

def get_similar_products(product_id,top_n=10):
    vectorizer=TfidfVectorizer(stop_words='english')
    product_descriptions=Product.objects.values_list('description',flat=True)
    tfidf_matrix=vectorizer.fit_transform(product_descriptions)
    target_product=Product.objects.get(id=product_id)
    all_products=list(Product.objects.all())
    target_index=all_products.index(target_product)
    cosine_sim=cosine_similarity(tfidf_matrix[target_index],tfidf_matrix).flatten()
    similar_indices=cosine_sim.argsort()[-top_n-1:-1][::-1]
    similar_indices=[i for i in similar_indices if i!=target_index]
    similar_products=[]
    for index in similar_indices:
        similar_products.append(all_products[index])
    return similar_products
