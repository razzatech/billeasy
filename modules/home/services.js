'use strict';

angular.module('Home')

.factory('HomeService',
    ['$http', '$cookieStore', '$rootScope', '$timeout',
    function ($http, $cookieStore, $rootScope, $timeout) {
        var service = {};

		service.renew_token = function (callback) {

			$http.get('http://billeasy.razzatech.com/api/_.py/renew_token?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
        };

        service.fetch_bills = function (callback) {

			$http.get('http://billeasy.razzatech.com/api/_.py/fetch_bills?token='+localStorage.getItem("token"))
			.success(function (response) {
                callback(response);
			});
        };

        return service;
    }])

