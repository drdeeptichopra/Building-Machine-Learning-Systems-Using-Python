#!/usr/bin/env python
# coding: utf-8

# In[13]:


from sklearn.decomposition import PCA
principalaxis = PCA(n_components=2)
principalaxis.fit(P)
PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
    svd_solver='auto', tol=0.0, whiten=False)

#Principal axis fit learns components and explained variance as follows:
print(principalaxis.components_)
print(principalaxis.explained_variance_)
def draw_vector(n0, n1, px=None):
    px = px or plt.gca()
    arrowprops=dict(arrowstyle='->',
                    linewidth=2,
                    shrinkA=0, shrinkB=0)
    px.annotate('', n1, n0, arrowprops=arrowprops)

# plot data
plt.scatter(P[:, 0], P[:, 1], alpha=0.2)
for length, vector in zip(principalaxis.explained_variance_, principalaxis.components_):
    p = vector * 3 * np.sqrt(length)
    draw_vector(principalaxis.mean_, principalaxis.mean_ + p)
plt.axis('equal');
def draw_vector(n0, n1, px=None):
    px = px or plt.gca()
    arrowprops=dict(arrowstyle='->',
                    linewidth=2,
                    shrinkA=0, shrinkB=0)
    px.annotate('', n1, n0, arrowprops=arrowprops)

# plot data
plt.scatter(P[:, 0], P[:, 1], alpha=0.2)
for length, vector in zip(principalaxis.explained_variance_, principalaxis.components_):
    p = vector * 3 * np.sqrt(length)
    draw_vector(principalaxis.mean_, principalaxis.mean_ + p)
plt.axis('equal');

principalaxis = PCA(n_components=1)
principalaxis.fit(P)
X_principalaxis = principalaxis.transform(P)
print("original shape:   ", P.shape)
print("transformed shape:", X_principalaxis.shape)

P_new = principalaxis.inverse_transform(X_principalaxis)
plt.scatter(P[:, 0], P[:, 1], alpha=0.2)
plt.scatter(P_new[:, 0], P_new[:, 1], alpha=0.8)
plt.axis('equal');


# In[ ]:





# In[ ]:




