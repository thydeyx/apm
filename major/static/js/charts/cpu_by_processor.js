/**
 * Created by yuyang on 15/3/11.
 */
/**
 * Created by yuyang on 15/3/11.
 */
require.config({
    paths: {
        echarts: '/static/js'
    }
});


require(
    [
        'echarts',
        'echarts/chart/bar',
        'echarts/chart/line',
        'echarts/chart/map',
        'echarts/chart/radar'
    ],
    function (ec) {
        //--- 折柱 ---
        var option;
        option = {
            title:{
                text:'CPU by Processor localdomain  2014/12/27    (0 threads not shown)',
                x:'center'
            },
            tooltip : {
                trigger: 'axis'
            },
            legend: {
                data:['User%','Sys%','Wait%'],
                x:'left'
            },

            calculable : true,
            xAxis : [
                {
                    type : 'category',

                    data : ['CPU001','CPU002','CPU003','CPU004']
                }
            ],
            yAxis : [
                {
                    type : 'value',
                    max:100
                }
            ],
            series : [
                {
                    name:'User%',
                    type:'bar',
                    stack: '总量',
                    itemStyle: {normal: {areaStyle: {type: 'default'}}},
                    data:[0.1, 0.0,0.0,46.7]
                },
                {
                    name:'Sys%',
                    type:'bar',
                    stack: '总量',
                    itemStyle: {normal: {areaStyle: {type: 'default'}}},
                    data:[0.2, 0.1, 0.0, 31.3]
                },
                {
                    name:'Wait%',
                    type:'bar',
                    stack: '总量',
                    itemStyle: {normal: {areaStyle: {type: 'default'}}},
                    data:[0.2, 0.1, 0.0, 0.0]
                }
            ]
        };








        var myChart1 = ec.init(document.getElementById('cpu_by_processor'));
        //var myChart2 = ec.init(document.getElementById('radar2'));
        //var myChart3 = ec.init(document.getElementById('radar3'));
        //var myChart4 = ec.init(document.getElementById('radar4'));
        //var myChart5 = ec.init(document.getElementById('radar5'));
        //var myChart6 = ec.init(document.getElementById('radar6'));
        //myChart1.setOption(option);
        //myChart2.setOption(option);
        //myChart3.setOption(option);
        //myChart4.setOption(option);
        //myChart5.setOption(option);
        myChart1.setOption(option);
    }
);