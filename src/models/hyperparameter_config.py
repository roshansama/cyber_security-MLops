PARAM_GRID = {

    # =========================
    # Random Forest
    # =========================

    "RandomForest": {

        'n_estimators': [
            100,
            200
        ],

        'max_depth': [
            10,
            20,
            None
        ],

        'min_samples_split': [
            2,
            5
        ],

        'min_samples_leaf': [
            1,
            2
        ],

        'max_features': [
            'sqrt',
            'log2'
        ]
    },


    # =========================
    # AdaBoost
    # =========================

    "AdaBoost": {

        'n_estimators': [
            50,
            100,
            200
        ],

        'learning_rate': [
            0.01,
            0.1,
            0.5,
            1.0
        ]
    },


    # =========================
    # XGBoost
    # =========================

    "XGBoost": {

        'n_estimators': [
            100,
            200
        ],

        'max_depth': [
            4,
            6,
            8
        ],

        'learning_rate': [
            0.01,
            0.05,
            0.1
        ],

        'subsample': [
            0.8,
            1.0
        ],

        'colsample_bytree': [
            0.8,
            1.0
        ],

        'gamma': [
            0,
            0.1,
            0.3
        ]
    },


    # =========================
    # LightGBM
    # =========================

    "LightGBM": {

        'n_estimators': [
            100,
            200
        ],

        'learning_rate': [
            0.01,
            0.05,
            0.1
        ],

        'num_leaves': [
            31,
            63,
            127
        ],

        'max_depth': [
            -1,
            10,
            20
        ],

        'subsample': [
            0.8,
            1.0
        ],

        'colsample_bytree': [
            0.8,
            1.0
        ]
    },


    # =========================
    # CatBoost
    # =========================

    "CatBoost": {

        'iterations': [
            100,
            200
        ],

        'depth': [
            4,
            6,
            8
        ],

        'learning_rate': [
            0.01,
            0.05,
            0.1
        ],

        'l2_leaf_reg': [
            1,
            3,
            5
        ]
    }
}