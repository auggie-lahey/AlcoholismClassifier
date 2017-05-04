import mlpy
pca = mlpy.PCA()
cols = [ 'home_life', 'failures', 'extra_school_support', 'free_time', 'absences', 'mom_edu']
# 'home_life', 'failures' 'extra_school_support 'free_time' 'absences'
newData = df[cols]
newData = newData.as_matrix()

pca.learn(newData)

z1 = pca.transform(newData, 1)
z3 = pca.transform(newData, 3)
z5 = pca.transform(newData, 5)


x_est_1 = pca.transform_inv(z1)
x_est_3 = pca.transform_inv(z3)
x_est_5 = pca.transform_inv(z5)


x_est_1_train = [x_est_1[i] for i in train.index]
x_est_1_train = np.array(x_est_1_train)
x_est_1_test = [x_est_1[i] for i in test.index]
x_est_1_test = np.array(x_est_1_test)

x_est_3_train = [x_est_3[i] for i in train.index]
x_est_3_train = np.array(x_est_3_train)
x_est_3_test = [x_est_3[i] for i in test.index]
x_est_3_test = np.array(x_est_3_test)

x_est_5_train = [x_est_5[i] for i in train.index]
x_est_5_train = np.array(x_est_5_train)
x_est_5_test = [x_est_5[i] for i in test.index]
x_est_5_test = np.array(x_est_5_test)
